#!/usr/bin/env python3
"""Copy entry.png next to this script into $MAKEFUN_OUTPUT_DIR/entry.png.

Standard library only. Fails loudly if MAKEFUN_OUTPUT_DIR is unset or
entry.png is missing, so a broken submission cannot pass silently.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not os.path.isfile(SRC):
        print("error: entry.png not found next to main.py: " + SRC,
              file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print("copied", SRC, "->", dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
