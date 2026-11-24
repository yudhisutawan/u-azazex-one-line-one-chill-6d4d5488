"""One Line, One Chill — make.fun entry (program/v1).

Writes a single sentence of horror (98 characters, one sentence) to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

Stdlib only. Writes nothing to the repository directory.

Revision note: docstring expanded and an exact-length guard added.
The written entry text is unchanged, so program output is byte-identical.
"""

import os
import sys

ENTRY = (
    "My name appeared in this morning's obituaries, "
    "and the photograph they used was taken an hour ago."
)


def main() -> int:
    text = ENTRY
    assert len(text) == 98, f"unexpected entry length {len(text)}"
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} outside 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
