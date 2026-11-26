"""Funniest Autocorrect Fail entry: write one autocorrect fail line.

The line is an autocorrect slip where 'deploy Friday' became 'destroy
Friday' and the servers took it as a suggestion. Standard library only,
no network.
"""

import os

LINE = "My autocorrect changed 'deploy Friday' to 'destroy Friday,' and honestly, the servers took it as a suggestion."


def write_entry(line):
    if not 1 <= len(line) <= 199:
        raise ValueError("line must be 1-199 chars, got %d" % len(line))
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
    write_entry(LINE)


if __name__ == "__main__":
    main()
