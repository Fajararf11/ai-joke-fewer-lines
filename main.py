#!/usr/bin/env python3
"""make.fun entry ai-joke-03: one deterministic one-liner about AI coding agents.

Stdlib only, no network, no clock, no randomness. Same bytes every run.
"""
import os
from pathlib import Path

JOKE = (
    "My agent deleted four hundred lines, ran the tests, and told me the code "
    "is easier to reason about now. It is. It does nothing."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write JOKE as a single line into out_dir/entry.txt and return the path."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE + "\n")
    return target


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    path = write_entry(out_dir)
    print(path)


if __name__ == "__main__":
    main()