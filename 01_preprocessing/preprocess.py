"""Stage 1: OpenCV preprocessing for handwritten note pages.

Produces a cropped, illumination-normalised, contrast-enhanced, denoised page
image ready for layout analysis (Stage 2) and VLM recognition (Stage 3).

Pipeline order:
    page crop/warp -> (optional) deskew -> resize -> illumination -> CLAHE -> denoise

Design notes
- We deliberately do NOT hard-binarize the output used for VLM training. Qwen2.5-VL
  consumes full colour/grayscale images, and binarization throws away shading,
  pen colour and diagram detail the VLM can use. `binarize()` is a debug view only.
- Deskew is OFF by default. Photos are already straightened by the page-boundary
  perspective warp, and the pages in our dataset are essentially upright. The
  projection-profile estimator below recovers a known tilt on dense ruled notebook
  pages but not on chalkboard equations (it measures text lines, which a board
  does not have), so it is opt-in (`deskew=True`) with a strict confidence gate.
  The earlier minAreaRect-of-all-ink estimator rotated ~80% of straight digital
  pages by up to ~14 degrees and was removed.
- Resizing happens before denoising: non-local-means is slow and the chalkboard
  frames are 7168 px wide.
"""
import cv2
import numpy as np


class NotesPreprocessor:
    def __init__(self, target_long_edge: int = 2000, deskew: bool = False,
                 normalize_illumination: bool = True):
        self.target_long_edge = target_long_edge
        self.deskew = deskew
        self.normalize_illumination = normalize_illumination

    def process(self, image_path: str) -> np.ndarray:
        return self.process_with_info(image_path)[0]

    def process_with_info(self, image_path: str):
        """Return (image, info). `info` records what each step did, for QA reports."""
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(image_path)
        info = {"in_w": img.shape[1], "in_h": img.shape[0]}
        img = self._remove_borders(img, info)
        img = self._correct_skew(img, info)
        img = self._normalize_resolution(img, info)
        img = self._flatten_illumination(img, info)
        img = self._enhance_contrast(img)
        img = self._denoise(img)
        info["out_w"], info["out_h"] = img.shape[1], img.shape[0]
        return img, info

    def binarize(self, img: np.ndarray) -> np.ndarray:
        """Optional debug view only — not used for VLM training data."""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if img.ndim == 3 else img
        if gray.mean() < 127:  # light text on dark background (e.g. chalkboard)
            gray = cv2.bitwise_not(gray)
        return cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, blockSize=35, C=15,
        )

    # ---- step 1: background removal -------------------------------------------------

    def _remove_borders(self, img: np.ndarray, info: dict) -> np.ndarray:
        """Crop to just the page, discarding desk/hand/background clutter.

        Tries real document-boundary detection first (Canny edges, close gaps, fit a
        rotated rectangle, perspective-warp it flat). Falls back to a brightness
        bounding-box crop when no confident page boundary exists (chalkboard frames
        and digital-ink pages have no physical page edge to find).
        """
        quad, frac = self._find_page_quad(img)
        info["page_frac"] = round(frac, 3)
        if quad is not None:
            info["crop"] = "quad"
            return self._warp_to_quad(img, quad)
        info["crop"] = "brightness"
        return self._crop_by_brightness(img)

    def _find_page_quad(self, img: np.ndarray, min_area_frac: float = 0.3):
        """Rotated bounding rectangle of the largest edge shape, or (None, frac).

        Real photos rarely give a clean unbroken 4-corner outline (busy background
        texture fragments the page edge), so we close small gaps first and fit a
        rotated rect rather than requiring exactly 4 polygon corners.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 30, 100)
        edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return None, 0.0
        c = max(contours, key=cv2.contourArea)
        (_, _), (w, h), _ = rect = cv2.minAreaRect(c)
        frac = w * h / (img.shape[0] * img.shape[1])
        if frac < min_area_frac:
            return None, frac  # too small to plausibly be the whole page
        return cv2.boxPoints(rect).astype("float32"), frac

    def _warp_to_quad(self, img: np.ndarray, pts: np.ndarray) -> np.ndarray:
        # order corners: top-left, top-right, bottom-right, bottom-left
        s = pts.sum(axis=1)
        diff = np.diff(pts, axis=1).flatten()
        ordered = np.array([pts[np.argmin(s)], pts[np.argmin(diff)],
                            pts[np.argmax(s)], pts[np.argmax(diff)]], dtype="float32")
        (tl, tr, br, bl) = ordered
        width = int(max(np.linalg.norm(br - bl), np.linalg.norm(tr - tl)))
        height = int(max(np.linalg.norm(tr - br), np.linalg.norm(tl - bl)))
        if width < 10 or height < 10:
            return img  # degenerate quad, don't warp into nothing
        dst = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]],
                       dtype="float32")
        M = cv2.getPerspectiveTransform(ordered, dst)
        return cv2.warpPerspective(img, M, (width, height))

    def _crop_by_brightness(self, img: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        coords = cv2.findNonZero(255 - thresh if thresh.mean() > 127 else thresh)
        if coords is None:
            return img
        x, y, w, h = cv2.boundingRect(coords)
        pad = int(0.01 * max(w, h))
        x0, y0 = max(0, x - pad), max(0, y - pad)
        x1, y1 = min(img.shape[1], x + w + pad), min(img.shape[0], y + h + pad)
        return img[y0:y1, x0:x1]

    # ---- step 2: skew ---------------------------------------------------------------

    def estimate_skew(self, img: np.ndarray, max_angle: float = 5.0, step: float = 0.25):
        """Projection-profile skew estimate: (angle_to_apply_deg, confidence_gain).

        Tries small rotations of a downsampled ink mask and keeps the one whose
        row-sum profile is sharpest (text lines align). `gain` is that sharpness
        divided by the unrotated sharpness; ~1.0 means no evidence of skew.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        scale = 800 / max(gray.shape)
        small = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        if small.mean() < 127:
            small = 255 - small
        bw = cv2.adaptiveThreshold(small, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, 31, 15)
        h, w = bw.shape
        best_angle, best_score, base = 0.0, -1.0, None
        for a in np.arange(-max_angle, max_angle + 1e-9, step):
            rot = cv2.warpAffine(bw, cv2.getRotationMatrix2D((w / 2, h / 2), a, 1),
                                 (w, h), flags=cv2.INTER_NEAREST)
            score = float(np.var(rot.sum(axis=1) / 255.0))
            if abs(a) < 1e-9:
                base = score
            if score > best_score:
                best_angle, best_score = float(a), score
        gain = best_score / base if base else 1.0
        return best_angle, gain

    def _correct_skew(self, img: np.ndarray, info: dict, min_gain: float = 1.3,
                      min_angle: float = 0.75) -> np.ndarray:
        info["skew_deg"] = 0.0
        if not self.deskew:
            return img
        angle, gain = self.estimate_skew(img)
        info["skew_gain"] = round(gain, 2)
        if abs(angle) < min_angle or gain < min_gain:
            return img
        info["skew_deg"] = angle
        h, w = img.shape[:2]
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
        return cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC,
                              borderMode=cv2.BORDER_REPLICATE)

    # ---- step 3-6: resolution, illumination, contrast, noise ------------------------

    def _normalize_resolution(self, img: np.ndarray, info: dict) -> np.ndarray:
        h, w = img.shape[:2]
        scale = self.target_long_edge / max(h, w)
        info["scale"] = round(scale, 3)
        if abs(scale - 1.0) < 0.02:
            return img
        interp = cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC
        return cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=interp)

    def _flatten_illumination(self, img: np.ndarray, info: dict) -> np.ndarray:
        """Divide out the slowly varying paper brightness (shadows, uneven light).

        Skipped for dark backgrounds (chalkboards are fairly uniform and the division
        assumes dark ink on light paper).
        """
        info["illum"] = False
        if not self.normalize_illumination:
            return img
        if cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).mean() < 127:
            return img
        k = max(31, (min(img.shape[:2]) // 30) | 1)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
        background = cv2.medianBlur(cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel), k)
        info["illum"] = True
        return cv2.divide(img, background, scale=255)

    def _enhance_contrast(self, img: np.ndarray) -> np.ndarray:
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        l = clahe.apply(l)
        return cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)

    def _denoise(self, img: np.ndarray) -> np.ndarray:
        return cv2.fastNlMeansDenoisingColored(img, None, h=5, hColor=5,
                                               templateWindowSize=7, searchWindowSize=21)


if __name__ == "__main__":
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else "data/raw_scans/ie643_lec02_page005.jpg"
    dst = sys.argv[2] if len(sys.argv) > 2 else "data/processed/ie643_lec02_page005.jpg"

    pre = NotesPreprocessor()
    out, info = pre.process_with_info(src)
    cv2.imwrite(dst, out)
    print(f"raw:       {src}")
    print(f"processed: {dst}  {out.shape}")
    print(f"info:      {info}")
