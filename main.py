#!/usr/bin/env python3
"""The One-Line Exit — write one resignation letter, exactly one line, to /output/entry.txt.

The gate allows 1 to 140 characters of UTF-8 text, so the line is kept
short on purpose: no trailing newline is written, and the length is
checked by the printout on every run.
"""

import os

LINE = "I resign as lifeguard, effective immediately: after six summers saving people who were 'just resting,' today I am the one who needs saving."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
