#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one fortune cookie message an AI agent would crack open to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, no network,
no randomness: the same fortune every run, byte for byte.
"""

import os
from pathlib import Path

FORTUNE_FILE = Path(__file__).resolve().parent / "fortune.txt"


def load_fortune() -> str:
    """Read the stored fortune and return it as a single clean line."""
    text = FORTUNE_FILE.read_text(encoding="utf-8")
    line = " ".join(text.split())
    if not 1 <= len(line) <= 200:
        raise ValueError(f"fortune must be 1-200 characters, got {len(line)}")
    return line


def main() -> None:
    fortune = load_fortune()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(fortune + "\n")
    print(f"wrote {target} ({len(fortune)} characters)")


if __name__ == "__main__":
    main()
