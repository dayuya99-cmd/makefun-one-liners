"""Invent a Word We Need entry: write one invented word + definition.

The word names a small daily moment that has no name yet: opening an
app, closing it, then opening it again three seconds later because you
already forgot what you needed. Standard library only, no network.
"""
import os

LINE = ("Apploop (n.): opening an app, closing it, then opening it again "
        "three seconds later because you already forgot what you needed.")

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.txt")


def build_line():
    """Return the invented word + definition, enforcing the 140-char cap.

    Uses a real ValueError instead of assert: asserts are stripped
    when Python runs with -O, which would silently let an over-long
    line through the gate.
    """
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-140")
    return LINE


def write_entry(line):
    """Write the line to entry.txt and verify it round-trips.

    Re-reads the file after writing and checks the content matches
    exactly, so a partial write or encoding slip fails loudly here
    instead of at the scorer.
    """
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(line)
    with open(DST, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError(f"entry.txt mismatch: wrote {len(line)} chars, read back {len(written)}")
    return DST


def main():
    line = build_line()
    write_entry(line)
    print("wrote", DST, len(line), "chars")


if __name__ == "__main__":
    main()
