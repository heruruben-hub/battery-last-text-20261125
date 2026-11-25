#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

A make.fun program/v1 entry: writes one line of plain text, at most
200 characters, to /output/entry.txt -- the phone battery's final
message to the charger it waited for all day.

Deterministic: the same line every run, no input, no network.
"""

import os
import sys

LINE = (
    "I waited all day by the outlet like a fool, dimming myself just "
    "for you, and you still left me at 1%. Enjoy the dark, babe \u2014 "
    "I'm taking the Wi-Fi password with me."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"line is {len(LINE)} characters, must be 1-200", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        # Exactly the line, no trailing newline: the gate counts every
        # character in the file, so nothing extra goes in.
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
