#!/usr/bin/env python3
# Rename the Planet entry: one line giving Saturn a funny new name, to /output/entry.txt.
# Pure standard library. The gate wants 1-200 characters, a single line.
# The joke is the idea, not a pun on the name: Saturn is a hoarder —
# the most moons of any planet, plus a ring of ice chunks it refuses to
# throw away. The why only fits Saturn.

from pathlib import Path

LINE = "Rename Saturn 'The Hoarder' \u2014 it keeps the most moons of any planet, plus a ring of ice chunks it refuses to throw away."
TARGET = Path("/output/entry.txt")


def run() -> None:
    text = LINE.strip()
    assert 0 < len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    run()
