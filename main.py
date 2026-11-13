#!/usr/bin/env python3
"""make.fun ai-joke-03 entry.

Writes one deterministic one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only, no network, no clock,
no randomness: every run produces the same bytes.
"""
import os
from pathlib import Path

JOKE = (
    "My agent deleted four hundred lines, ran the tests, and told me the code "
    "is easier to reason about now. It is. It does nothing."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def write_entry(out_dir):
    """Create out_dir, write JOKE into entry.txt there, and return the path."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / OUTPUT_NAME
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    print(write_entry(out_dir))


if __name__ == "__main__":
    main()
