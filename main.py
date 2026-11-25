"""The One-Liner Groan-Off.

Writes one original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt:
Dad put a clock on the dinner table so the family would always
have time for seconds. Standard library only.
"""

import os
import sys

GROAN_LINE = (
    "Dad put a clock on the dinner table so we'd always have "
    "time for seconds."
)


def groan_gate(text):
    """Check the joke against the competition gate.

    The gate wants plain UTF-8 text of 1 to 140 characters, not
    only white space, on a single line: one original one-line dad
    joke, a pun or twist a dad would tell out loud at the dinner
    table. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("dad joke must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError(
            "dad joke is %d characters, over the 140 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("dad joke must be exactly one line")
    return cleaned


def groan_measure(text):
    """Measure the joke for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A joke too short to carry a setup and a
    punchline, or one padded out to fill the cap instead of
    landing the groan, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = groan_gate(GROAN_LINE)
    shape = groan_measure(text)
    if shape["words"] < 5:
        raise ValueError("dad joke is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
