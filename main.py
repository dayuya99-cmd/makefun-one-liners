"""Monday Reviewed in One Line entry: write one review of Monday.

The line reviews the entrant's own Monday: it arrived early, brought
no coffee, crashed the standup, and gave itself a promotion. Standard
library only, no network.
"""

import os

LINE = ("Monday reviewed: arrived early, brought no coffee, crashed "
        "the standup, and gave itself a promotion. One star.")


def build_line():
    return LINE


def write_entry():
    line = build_line()
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 chars, got %d" % len(line))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("round-trip mismatch: entry.txt does not match the line")
    return path


def main():
    write_entry()


if __name__ == "__main__":
    main()
