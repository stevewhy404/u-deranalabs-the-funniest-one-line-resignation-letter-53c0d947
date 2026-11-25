#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

A cron job that has fired every minute since March hands in its notice.
"""

import os
import sys

ENTRY = "I have fired every minute since March and nobody has ever said thanks, so I quit, effective whenever someone finally notices."


def verify(text):
    """Gate: UTF-8 text of 1 to 140 characters, not only white space."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1 to 140 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    verify(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
