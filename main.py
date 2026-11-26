#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261126 bounty.

Copies the bundled entry.png byte-for-byte to /output/entry.png.
Deterministic: stdlib only, no network, no randomness, no timestamps.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = "/output"
    destination = os.path.join(output_dir, "entry.png")

    os.makedirs(output_dir, exist_ok=True)
    if not os.path.isfile(source):
        print(f"error: bundled image not found: {source}", file=sys.stderr)
        return 1
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
