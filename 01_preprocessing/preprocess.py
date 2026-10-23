"""Stage 1: OpenCV preprocessing for handwritten note pages.

Produces a deskewed, denoised, contrast-enhanced page image ready for
layout analysis (Stage 2) and VLM recognition (Stage 3).

Design note: unlike a classical OCR pipeline, we deliberately do NOT
hard-binarize the output used for VLM training. Qwen2.5-VL consumes full
color/grayscale images, and binarization throws away shading, pen-color
and diagram detail the VLM can actually use. `binarize()` is kept as a
separate, optional debug view (e.g. to sanity-check skew correction),
not part of the default pipeline.
"""
import cv2
import numpy as np


class NotesPreprocessor:
    def __init__(self, target_long_edge: int = 2000):
        self.target_long_edge = target_long_edge

    def process(self, image_path: str) -> np.ndarray:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(image_path)
        img = self._remove_borders(img)
        img = self._correct_skew(img)
        img = self._enhance_contrast(img)
        img = self._denoise(img)
        img = self._normalize_resolution(img)
        return img

    def binarize(self, img: np.ndarray) -> np.ndarray:
        """Optional debug view only — not used for VLM training data."""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if img.ndim == 3 else img
        if gray.mean() < 127:  # light text on dark background (e.g. chalkboard)
            gray = cv2.bitwise_not(gray)
        return cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, blockSize=35, C=15,
        )

    def _remove_borders(self, img: np.ndarray) -> np.ndarray:
        """Crop to just the page, discarding desk/hand/background clutter.

        Tries real document-boundary detection first (find the page's actual
        4-cornered edge via Canny + contours, then perspective-warp it flat —
        this is what separates "page" from "background", not just a brightness
        cutoff). Falls back to the old brightness-bounding-box crop when no
        confident quadrilateral is found (e.g. a digital-ink screenshot has no
        physical page edge to find).
        """
        quad = self._find_page_quad(img)
        if quad is not None:
            return self._warp_to_quad(img, quad)
        return self._crop_by_brightness(img)

    def _find_page_quad(self, img: np.ndarray, min_area_frac: float = 0.3):
        """Find the page's rotated bounding rectangle from its (possibly broken-up)
        edge contour. Real photos rarely give a clean unbroken 4-corner outline --
        busy background texture fragments the page edge into many small pieces --
        so we close small gaps first, then fit a rotated rect to the largest
        resulting shape rather than requiring exactly 4 polygon corners.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 30, 100)
        edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return None
        img_area = img.shape[0] * img.shape[1]
        c = max(contours, key=cv2.contourArea)
        rect = cv2.minAreaRect(c)
        (_, _), (w, h), _ = rect
        if w * h < min_area_frac * img_area:
            return None  # too small to plausibly be the whole page
        return cv2.boxPoints(rect).astype("float32")

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

    def _correct_skew(self, img: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        if thresh.mean() > 127:  # ensure foreground (ink/chalk) is white for minAreaRect
            thresh = 255 - thresh
        coords = cv2.findNonZero(thresh)
        if coords is None:
            return img
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        if abs(angle) < 0.5 or abs(angle) > 20:
            return img  # ignore noise / bogus large angles
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC,
                               borderMode=cv2.BORDER_REPLICATE)

    def _enhance_contrast(self, img: np.ndarray) -> np.ndarray:
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        l = clahe.apply(l)
        return cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)

    def _denoise(self, img: np.ndarray) -> np.ndarray:
        return cv2.fastNlMeansDenoisingColored(img, None, h=5, hColor=5,
                                                templateWindowSize=7, searchWindowSize=21)

    def _normalize_resolution(self, img: np.ndarray) -> np.ndarray:
        h, w = img.shape[:2]
        scale = self.target_long_edge / max(h, w)
        if abs(scale - 1.0) < 0.02:
            return img
        interp = cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC
        return cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=interp)


if __name__ == "__main__":
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else "data/raw_scans/ie643_lec02_page005.jpg"
    dst = sys.argv[2] if len(sys.argv) > 2 else "data/processed/ie643_lec02_page005.jpg"
    dbg = sys.argv[3] if len(sys.argv) > 3 else "data/processed/ie643_lec02_page005_binarized_debug.jpg"

    pre = NotesPreprocessor()
    out = pre.process(src)
    cv2.imwrite(dst, out)
    cv2.imwrite(dbg, pre.binarize(out))
    print(f"raw:       {src}")
    print(f"processed: {dst}  {out.shape}")
    print(f"debug bin: {dbg}")
