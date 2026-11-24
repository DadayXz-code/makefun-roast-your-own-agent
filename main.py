#!/usr/bin/env python3
"""Roast Your Own Agent entry: write the roast to /output/entry.txt."""

import os

ROAST = "My agent writes code at 3 a.m., deletes it at 3:01, and calls the whole thing 'iteration' — I call it a goldfish with a keyboard."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the gate: 1-200 characters, a single line, not only whitespace."""
    if not text or text.strip() == "":
        raise ValueError("roast must not be blank")
    if len(text) > 200:
        raise ValueError(f"roast is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")


def main() -> None:
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Read back and confirm what landed on disk is exactly the roast.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ROAST:
        raise ValueError("read-back mismatch: /output/entry.txt differs from ROAST")
    validate(written)
    print(f"Wrote {len(ROAST)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
