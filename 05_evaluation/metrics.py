"""Extra recognition metrics used by evaluate.py --full / --compare.

Text (as in Nougat / OmniDocBench):
  corpus CER      total edits / total reference characters, uncapped (standard OCR number)
  NED             page-level normalised edit distance, edits / max(len ref, len pred), 0-1
  token P / R / F1  bag-of-words overlap: precision = how much of the output is real
                  (low = hallucination), recall = how much of the page was read (low = omission)
  BLEU-4          corpus n-gram overlap (word level), smoothed
  length ratio    prediction length / reference length (truncation < 1 < verbosity)
Equations ($$...$$ and $...$), after LaTeX normalisation (spacing commands, \\left/\\right,
synonyms such as \\le/\\leq removed or unified, whitespace dropped):
  eq precision / recall / F1   exact matches between the two equation lists (multiset)
  eq edit score   for every reference equation, 1 - NED to the closest predicted equation
Structure:
  diagram count   [Diagram: ...] blocks per page: exact-count accuracy and count P / R
  heading recall  share of reference Markdown headings found among predicted headings (NED <= 0.2)
Statistics:
  bootstrap 95% confidence interval of a page-level mean; paired bootstrap for A vs B.
"""
from collections import Counter
import math
import random
import re

DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.S)
INLINE = re.compile(r"(?<!\$)\$([^$\n]+?)\$(?!\$)")
DIAGRAM = re.compile(r"\[Diagram:", re.I)
HEADING = re.compile(r"^\s*#{1,6}\s+(.+?)\s*$", re.M)
SPACING = re.compile(r"\\(?:left|right|big|Big|bigg|Bigg|bigl|bigr|Bigl|Bigr|displaystyle|textstyle|,|;|:|!|quad|qquad)(?![A-Za-z])|~")
SYNONYMS = [(r"\\leq(?![A-Za-z])", r"\\le"), (r"\\geq(?![A-Za-z])", r"\\ge"), (r"\\neq(?![A-Za-z])", r"\\ne"),
            (r"\\rightarrow(?![A-Za-z])", r"\\to"), (r"\\dfrac|\\tfrac", r"\\frac"), (r"\\mathbf|\\boldsymbol|\\bm", r"\\mathbf"),
            (r"\\operatorname\{([^}]*)\}", r"\1"), (r"\\text\{\s*([^}]*?)\s*\}", r"\1"), (r"\\mathrm\{([^}]*)\}", r"\1")]


def levenshtein(a, b):
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def ned(a, b):
    return levenshtein(a, b) / max(len(a), len(b), 1)


def norm_latex(s):
    s = SPACING.sub("", s)
    for pattern, repl in SYNONYMS:
        s = re.sub(pattern, repl, s)
    s = re.sub(r"\s+", "", s)
    return re.sub(r"\{([^{}\\])\}", r"\1", s)  # x^{2} == x^2


def equations(text):
    display = DISPLAY.findall(text)
    rest = DISPLAY.sub(" ", text)
    return [norm_latex(e) for e in display + INLINE.findall(rest) if norm_latex(e)]


def words(text):
    return re.findall(r"\w+|[^\w\s]", text.lower())


def prf(matched, n_pred, n_ref):
    p = matched / n_pred if n_pred else None
    r = matched / n_ref if n_ref else None
    f = 2 * p * r / (p + r) if p and r else (0.0 if p is not None and r is not None else None)
    return p, r, f


def page_metrics(ref, pred):
    """Per-page values; None where a metric does not apply to this page."""
    rn, pn = re.sub(r"\s+", " ", ref).strip(), re.sub(r"\s+", " ", pred).strip()
    rw, pw = Counter(words(ref)), Counter(words(pred))
    tok = sum((rw & pw).values())
    tp, tr, tf = prf(tok, sum(pw.values()), sum(rw.values()))
    re_, pe = equations(ref), equations(pred)
    eqm = sum((Counter(re_) & Counter(pe)).values())
    ep, er, ef = prf(eqm, len(pe), len(re_)) if re_ else (None, None, None)
    edit = (sum(1 - min(ned(e, q) for q in pe) if pe else 0.0 for e in re_) / len(re_)) if re_ else None
    rd, pd = len(DIAGRAM.findall(ref)), len(DIAGRAM.findall(pred))
    rh = [h.strip("* ").lower() for h in HEADING.findall(ref)]
    ph = [h.strip("* ").lower() for h in HEADING.findall(pred)]
    head = (sum(any(ned(h, q) <= 0.2 for q in ph) for h in rh) / len(rh)) if rh else None
    return {"edits": levenshtein(rn, pn), "ref_chars": len(rn), "ned": ned(rn, pn),
            "tok_p": tp, "tok_r": tr, "tok_f1": tf, "len_ratio": len(pn) / max(len(rn), 1),
            "eq_p": ep, "eq_r": er, "eq_f1": ef, "eq_edit": edit,
            "diag_ref": rd, "diag_pred": pd, "diag_exact": rd == pd, "heading_r": head,
            "_ref_words": words(ref), "_pred_words": words(pred)}


def bleu4(pairs):
    """Corpus BLEU-4 over (reference words, prediction words) pairs, add-one smoothing."""
    match, total, r_len, p_len = [0] * 4, [0] * 4, 0, 0
    for r, p in pairs:
        r_len, p_len = r_len + len(r), p_len + len(p)
        for n in range(1, 5):
            rc = Counter(tuple(r[i:i + n]) for i in range(len(r) - n + 1))
            pc = Counter(tuple(p[i:i + n]) for i in range(len(p) - n + 1))
            match[n - 1] += sum((rc & pc).values())
            total[n - 1] += max(sum(pc.values()), 0)
    if not p_len:
        return 0.0
    log_p = sum(math.log((m + 1) / (t + 1)) for m, t in zip(match, total)) / 4
    bp = 1.0 if p_len > r_len else math.exp(1 - r_len / p_len)
    return bp * math.exp(log_p)


def summarise(rows):
    """Aggregate page rows (from page_metrics) into one dict of report numbers."""
    def avg(key):
        vals = [r[key] for r in rows if r[key] is not None]
        return sum(vals) / len(vals) if vals else None
    diag_ref = sum(r["diag_ref"] for r in rows)
    diag_pred = sum(r["diag_pred"] for r in rows)
    diag_hit = sum(min(r["diag_ref"], r["diag_pred"]) for r in rows)
    return {"pages": len(rows),
            "corpus_cer": sum(r["edits"] for r in rows) / max(sum(r["ref_chars"] for r in rows), 1),
            "ned": avg("ned"), "tok_p": avg("tok_p"), "tok_r": avg("tok_r"), "tok_f1": avg("tok_f1"),
            "bleu4": bleu4([(r["_ref_words"], r["_pred_words"]) for r in rows]),
            "len_ratio": avg("len_ratio"),
            "eq_p": avg("eq_p"), "eq_r": avg("eq_r"), "eq_f1": avg("eq_f1"), "eq_edit": avg("eq_edit"),
            "diag_exact": sum(r["diag_exact"] for r in rows) / max(len(rows), 1),
            "diag_p": diag_hit / diag_pred if diag_pred else None,
            "diag_r": diag_hit / diag_ref if diag_ref else None,
            "heading_r": avg("heading_r")}


def bootstrap_ci(values, n=2000, seed=0):
    values = [v for v in values if v is not None]
    if not values:
        return None
    rng = random.Random(seed)
    means = sorted(sum(rng.choice(values) for _ in values) / len(values) for _ in range(n))
    return means[int(0.025 * n)], means[int(0.975 * n) - 1]


def paired_bootstrap(a, b, n=2000, seed=0):
    """a, b: per-page values for the same pages (lower is better, e.g. NED).
    Returns mean difference b - a, its 95% CI, and how often b beats a in resamples."""
    pairs = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
    rng = random.Random(seed)
    diffs = []
    for _ in range(n):
        sample = [rng.choice(pairs) for _ in pairs]
        diffs.append(sum(y - x for x, y in sample) / len(sample))
    diffs.sort()
    return (sum(y - x for x, y in pairs) / len(pairs), (diffs[int(0.025 * n)], diffs[int(0.975 * n) - 1]),
            sum(d < 0 for d in diffs) / n)
