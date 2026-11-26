#!/usr/bin/env python3
"""Write the winning one-star review of the Moon to /output/entry.txt.

Deterministic: the same single line is written on every run, with no
trailing newline, so the output is exactly 82 UTF-8 characters.
"""

import os

ENTRY = "One star. We planted a flag there in 1969 and it hasn't done a single thing since."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
