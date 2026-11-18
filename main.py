#!/usr/bin/env python3
"""Entry point for make.fun news-image-20261117.

Copies the pre-rendered entry.png (shipped in this repo) to the output
directory. Standard library only: no network, no randomness, no clock,
so repeated runs produce byte-identical output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
