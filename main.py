#!/usr/bin/env python3
"""Warning-label entry: copies the entry line into the grader output dir.

Reads entry.txt shipped beside this script and writes it, byte for byte,
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is unset). Uses one direct write only: no temporary file, no rename, so
the output keeps the explicit 0644 mode the grader needs to read it.
"""

import os
from pathlib import Path


def main():
    src = Path(__file__).resolve().parent / "entry.txt"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        data = src.read_bytes()
        out = out_dir / "entry.txt"
        out.write_bytes(data)
        os.chmod(out, 0o644)
    except OSError as exc:
        raise SystemExit(f"cannot write entry output: {exc}") from exc


if __name__ == "__main__":
    main()
