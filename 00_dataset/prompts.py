"""The two training-example 'instructions', in one place.

Everything else — the model, the JSONL format, the training loop — is identical for
both. The only thing that differs is this text, because it's just a string sitting
inside each training example's user turn, not a mode switch anywhere else. Both
build_dataset.py (our 205 pages) and build_external_dataset.py (public equation
datasets) import from here, so there is exactly one place that defines what each
instruction says.
"""

PAGE_PROMPT = (
    "Convert this handwritten lecture note page to clean structured Markdown. "
    "Use LaTeX ($$...$$) for all math equations. Preserve headings (#, ##), "
    "bullet points, numbering, and logical structure."
)

EQUATION_PROMPT = "Convert this handwritten mathematical expression to LaTeX."


def build_record(image_path, prompt, ground_truth):
    """One training example: an image + an instruction, paired with the correct answer.

    Used for both page-level examples (prompt=PAGE_PROMPT) and single-equation
    examples (prompt=EQUATION_PROMPT) — same shape either way, so the model just
    sees "some images come with instruction A, some come with instruction B" and
    learns to behave differently depending on which one it's given.
    """
    return {
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image_path},
                    {"type": "text", "text": prompt},
                ],
            },
            {"role": "assistant", "content": ground_truth},
        ]
    }
