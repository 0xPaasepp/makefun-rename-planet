#!/usr/bin/python3
"""New name for a planet, in one line.

Saturn keeps more moons than any other planet and holds on to a
ring of ice chunks — a hoarder, not a minimalist. The line names
the planet, the nickname, and the reason in a single breath.
"""

import os


def sentence():
    segments = (
        "Rename Saturn 'The Hoarder'",
        " \u2014 ",
        "it keeps the most moons of any planet, plus a ring of ice chunks it refuses to throw away.",
    )
    return "".join(segments)


def save(line):
    line = line.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.count("\n") == 0 and line.count("\r") == 0, "entry must be one line"
    folder = os.path.dirname("/output/entry.txt")
    os.makedirs(folder, exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return line


if __name__ == "__main__":
    print(save(sentence()))
