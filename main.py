#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt. No network, no input:
the text is fixed in this file.
"""

import os

TEXT = """In the garden bed my mother dug
I found a small brass key,
warm from the sun, its teeth smooth.

It fits no door in our house.
Not the shed. Not the cellar.
Not the chest by her bed.

Tonight I will try the gate at the end of the lane,
the one that has never once been locked."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
