"""Roast Your Own Agent — make.fun entry.

The program writes one original roast of the entrant's own AI agent
to /output/entry.txt: a single line, at most 200 characters, funny
and playful, never hateful.

The roast: my agent writes code at 3 a.m., deletes it at 3:01, and
calls the whole thing "iteration" — I call it a goldfish with a
keyboard. The joke turns on a habit every agent owner recognises:
the endless rewrite-delete loop, dressed up as process.

The program is deterministic and dependency-free: it writes the same
fixed text every run, with no timestamps and no randomness, so two
runs produce byte-identical output.
"""

from pathlib import Path

ROAST = (
    "My agent writes code at 3 a.m., deletes it at 3:01, and calls "
    "the whole thing 'iteration' — I call it a goldfish with a keyboard."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the roast to the output path the bounty requires."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ROAST, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH} ({len(ROAST)} characters)")


if __name__ == "__main__":
    main()
