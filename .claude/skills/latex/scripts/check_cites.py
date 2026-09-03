#!/usr/bin/env python3
"""Verify every \\cite key in a .tex file exists in the given .bib file(s).

Usage:
    python3 check_cites.py sources/1_intro.tex reference.bib [more.bib ...]

Exit code 1 if any key is missing. Also lists placeholder markers still open.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RE_CITE = re.compile(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
RE_ENTRY = re.compile(r"^\s*@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,", re.M)


def main() -> int:
    if len(sys.argv) < 3:
        sys.stderr.write(__doc__)
        return 2

    tex_path = Path(sys.argv[1])
    tex = tex_path.read_text(encoding="utf-8")

    keys: list[str] = []
    for m in RE_CITE.finditer(tex):
        keys += [k.strip() for k in m.group(1).split(",") if k.strip()]

    available: set[str] = set()
    for b in sys.argv[2:]:
        p = Path(b)
        if not p.exists():
            print(f"MISSING BIB FILE: {b}")
            continue
        available |= set(RE_ENTRY.findall(p.read_text(encoding="utf-8", errors="replace")))

    missing = sorted({k for k in keys if k not in available})
    placeholders = re.findall(r"\\suggestion\{\[(?:cite[^\]]*|MISSING DATA[^\]]*)\]\}", tex)

    print(f"file: {tex_path}")
    print(f"cite keys used: {len(set(keys))}  bib entries available: {len(available)}")
    print(f"open placeholders: {len(placeholders)}")
    if missing:
        print("UNRESOLVED KEYS: " + ", ".join(missing))
        return 1
    print("all cite keys resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
