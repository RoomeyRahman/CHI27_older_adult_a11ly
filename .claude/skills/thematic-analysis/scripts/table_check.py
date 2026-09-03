#!/usr/bin/env python3
"""Check that every markdown table under /output/codes/ renders, and that FINAL-CODEBOOK.md stays compact.

Catches the failures that make a codebook unreadable: rows with the wrong number of columns, a
missing separator row, a cell containing a line break, an unescaped pipe inside a quote, a table with
no blank line before it, and cells that have grown into paragraphs.

Usage:  python3 .claude/skills/thematic-analysis/scripts/table_check.py [repo_root] [slot]

`slot` (A1, A2, ...) restricts the check to /output/codes/<slot>/. Omit it to check everything.

Exit 0 = clean. Exit 1 = problems found. Exit 2 = paths missing.
"""

import os
import re
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
SLOT = sys.argv[2].upper() if len(sys.argv) > 2 else ""
OUT = os.path.join(ROOT, "output", "codes", SLOT) if SLOT else os.path.join(ROOT, "output", "codes")

# word caps for the six-column final table, by column index
FINAL_CAPS = {1: 20, 4: 25, 5: 20}
FINAL_COLS = 6
SEP = re.compile(r"^\|?[\s:|-]+\|[\s:|-]*$")


def split_row(line):
    """Split a markdown table row into cells, honouring escaped pipes."""
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|") and not body.endswith("\\|"):
        body = body[:-1]
    cells, cur, i = [], "", 0
    while i < len(body):
        if body[i] == "\\" and i + 1 < len(body) and body[i + 1] == "|":
            cur += "|"
            i += 2
            continue
        if body[i] == "|":
            cells.append(cur.strip())
            cur = ""
            i += 1
            continue
        cur += body[i]
        i += 1
    cells.append(cur.strip())
    return cells


def check_file(path, problems):
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()

    rel = os.path.relpath(path, ROOT)
    is_final = os.path.basename(path) == "FINAL-CODEBOOK.md"
    i = 0
    while i < len(lines):
        if not lines[i].strip().startswith("|"):
            i += 1
            continue

        start = i
        block = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            block.append((i + 1, lines[i]))
            i += 1

        if start > 0 and lines[start - 1].strip() != "" and not lines[start - 1].strip().startswith("|"):
            problems.append((rel, start + 1, "table has no blank line before it; it will not render"))

        if len(block) < 2 or not SEP.match(block[1][1].strip()):
            problems.append((rel, block[0][0], "table has no separator row (|---|---|) under its header"))
            continue

        header_cells = split_row(block[0][1])
        ncols = len(header_cells)
        if is_final and ncols != FINAL_COLS:
            problems.append((rel, block[0][0],
                             "final codebook table has %d columns, expected %d" % (ncols, FINAL_COLS)))

        for line_no, raw in block:
            if SEP.match(raw.strip()):
                continue
            cells = split_row(raw)
            if len(cells) != ncols:
                problems.append((rel, line_no,
                                 "row has %d cells, header has %d (an unescaped | inside a cell is the usual cause; write it as \\|)"
                                 % (len(cells), ncols)))
                continue
            for idx, cell in enumerate(cells):
                if "<br" in cell.lower():
                    problems.append((rel, line_no, "cell %d uses <br>; keep one line per row instead" % (idx + 1)))
                if cell.strip().startswith(("- ", "* ", "> ")):
                    problems.append((rel, line_no, "cell %d starts a list or block quote; tables cannot hold them" % (idx + 1)))
                if "[pending" in cell.lower() and is_final:
                    problems.append((rel, line_no, "final codebook still contains a pending marker"))
                if is_final and idx in FINAL_CAPS:
                    words = len(cell.split())
                    if words > FINAL_CAPS[idx]:
                        problems.append((rel, line_no,
                                         "cell %d is %d words, cap is %d; move the detail to the working files"
                                         % (idx + 1, words, FINAL_CAPS[idx])))
    return


def main():
    if not os.path.isdir(OUT):
        print("MISSING: %s (nothing written yet)" % OUT)
        return 2

    problems = []
    files = 0
    finals = []
    for dirpath, _dirs, names in os.walk(OUT):
        for name in sorted(names):
            if name.endswith(".md"):
                files += 1
                if name == "FINAL-CODEBOOK.md":
                    finals.append(os.path.join(dirpath, name))
                check_file(os.path.join(dirpath, name), problems)

    print("Markdown files checked: %d%s" % (files, (" in slot " + SLOT) if SLOT else ""))
    if not finals:
        print("NOTE: no FINAL-CODEBOOK.md found yet")

    if problems:
        print("FAIL: %d table problem(s)" % len(problems))
        print("---")
        for rel, line_no, why in problems:
            print("%s:%d  %s" % (rel, line_no, why))
        print("---")
        return 1

    print("PASS: all tables render and the final codebook is within its cell caps")
    return 0


if __name__ == "__main__":
    sys.exit(main())
