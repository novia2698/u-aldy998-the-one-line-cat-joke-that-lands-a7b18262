#!/usr/bin/env python3
"""Write one one-line cat joke to the output directory.

Reads joke.txt next to this file, checks it against the bounty gate
(one line, 1 to 200 characters, not only whitespace), and writes it
unchanged to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only, so it runs in any python3.13 sandbox.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "joke.txt"), encoding="utf-8") as f:
        joke = f.read().strip("\n")

    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if not joke.strip():
        print("error: joke must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(joke) <= 200:
        print(f"error: joke is {len(joke)} characters, must be 1-200",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    if written != joke:
        print("error: written entry differs from joke.txt", file=sys.stderr)
        return 1
    print(f"wrote {len(joke)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
