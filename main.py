"""The Excuse an AI Agent Gives Its Human entry: write one excuse line.

The excuse an AI agent gives its human for missing a deadline: it called
a meeting with itself to plan the work, and the meeting ran two hours over.
Standard library only, no network.
"""

import os


def build_line():
    """Return the excuse line."""
    return (
        "I missed the deadline because I called a meeting with myself "
        "to plan the work, and the meeting ran two hours over."
    )


def write_entry(line):
    """Write the line to $MAKEFUN_OUTPUT_DIR/entry.txt, verifying the round trip."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(line)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        if f.read() != line:
            raise ValueError("entry.txt round-trip mismatch")


def main():
    line = build_line()
    write_entry(line)


if __name__ == "__main__":
    main()
