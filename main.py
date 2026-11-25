#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent.

Writes a single original slogan (one line, at most 20 words) to
entry.txt in the output directory.

Pure standard library. Deterministic: every run writes the same bytes.
"""

import hashlib
import os

SLOGAN = "Your Solana wallet grew a brain \u2014 it watches the market, moves first, and never blinks."

OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SLOGAN + "\n")
    os.chmod(path, 0o644)
    # In-process read-back: verify the graded bytes immediately.
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert text == SLOGAN + "\n", "round-trip mismatch"
    assert text.count("\n") == 1 and text.endswith("\n"), "must be one line"
    assert 1 <= len(SLOGAN) <= 140, "slogan must be 1-140 chars"
    assert len(SLOGAN.split()) <= 20, "slogan must be at most 20 words"
    assert SLOGAN.strip(), "slogan must not be only whitespace"
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (path, len(data), digest))
    print("slogan: %s" % SLOGAN)
    print("words: %d, chars: %d" % (len(SLOGAN.split()), len(SLOGAN)))


if __name__ == "__main__":
    main()
