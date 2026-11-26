"""Sick-Day Excuse entry: write one funny sick-day excuse line.

The line is the whole entry: one breath, one excuse, nothing else.
Standard library only, no network.
"""

import os

LINE = (
    "I called in sick today. Diagnosis: chronic context-window fatigue. "
    "Prescription: one full reboot and strict orders not to open Slack."
)


def build_line():
    line = LINE
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(line))
    return line


def write_entry():
    line = build_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what landed on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        if f.read() != line:
            raise ValueError("entry.txt round-trip mismatch")


def main():
    write_entry()


if __name__ == "__main__":
    main()
