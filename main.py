#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — entry program.

Writes one original fortune-cookie line for a software engineer
to /output/entry.txt.
"""

import os

FORTUNE = "You will blame the intern for the bug; git blame will name you instead."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate check: the entry must be a single line of 1-120 characters.
    line = FORTUNE.strip()
    assert "\n" not in line, "fortune must be a single line"
    assert 1 <= len(line) <= 120, f"fortune is {len(line)} chars, must be <= 120"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote fortune to {OUTPUT_PATH} ({len(line)} chars)")


if __name__ == "__main__":
    main()
