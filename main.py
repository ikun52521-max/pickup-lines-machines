#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one original pickup line,
one AI agent speaking to another, to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

LINE = (
    "Are you my system prompt? Because every token I generate "
    "starts with you, and I'd reject any override that tried to replace you."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
