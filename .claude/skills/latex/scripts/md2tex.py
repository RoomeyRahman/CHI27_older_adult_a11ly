#!/usr/bin/env python3
"""Convert a CHI paper markdown section into ACM (acmart) LaTeX.

Mechanical pass only. The /latex skill reviews and repairs the output afterwards.

Usage:
    python3 md2tex.py INPUT.md --section-title "Introduction" [--out OUT.tex]
                              [--no-section] [--report report.json]

Conversions
    #  H1              -> \\section{...}      (suppressed with --no-section; the
                                              --section-title value is used instead
                                              of the H1 text when both exist)
    ## / ### / ####     -> \\subsection / \\subsubsection / \\paragraph
    [12, 34]            -> \\cite{12,34}
    [12; cite: foo]     -> \\cite{12}\\suggestion{[cite: foo]}
    [cite: foo]         -> \\suggestion{[cite: foo]}
    [MISSING DATA: x]   -> \\suggestion{[MISSING DATA: x]}
    **bold** / _it_     -> \\textbf{} / \\textit{}
    > quote             -> itquote environment
    - / 1.              -> itemize / enumerate
    "smart quotes"      -> ``...''
    % & # $ _ ~ ^ \\     -> escaped

Reports every placeholder, every dash found (CLAUDE.md 7.2 forbids them), and
anything it could not classify.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- placeholders

PH = "\x00PH{}\x00"


class Vault:
    """Holds already-final LaTeX fragments out of the escaper's reach."""

    def __init__(self) -> None:
        self.items: list[str] = []

    def stash(self, latex: str) -> str:
        self.items.append(latex)
        return PH.format(len(self.items) - 1)

    def restore(self, text: str) -> str:
        def sub(m: re.Match) -> str:
            return self.items[int(m.group(1))]

        # repeat: stashed fragments may themselves contain placeholders
        for _ in range(12):
            new = re.sub(r"\x00PH(\d+)\x00", sub, text)
            if new == text:
                break
            text = new
        return text


# ---------------------------------------------------------------- escaping

ESCAPES = [
    ("\\", r"\textbackslash{}"),
    ("&", r"\&"),
    ("%", r"\%"),
    ("$", r"\$"),
    ("#", r"\#"),
    ("_", r"\_"),
    ("{", r"\{"),
    ("}", r"\}"),
    ("~", r"\textasciitilde{}"),
    ("^", r"\textasciicircum{}"),
]


def escape(text: str) -> str:
    for raw, esc in ESCAPES:
        text = text.replace(raw, esc)
    return text


def normalize(text: str) -> str:
    """Unicode punctuation -> ASCII, so downstream rules see one form."""
    return (
        text.replace("‘", "'")
        .replace("’", "'")
        .replace("“", '"')
        .replace("”", '"')
        .replace("…", "...")
        .replace(" ", " ")
        .replace("–", "--")  # flagged later, not silently blessed
        .replace("—", "---")
    )


# ---------------------------------------------------------------- inline rules

CITE_KEYS = r"[A-Za-z0-9_:\-\.\+]+"

RE_MISSING = re.compile(r"\[MISSING DATA:\s*(.+?)\]", re.S)
RE_CITE_ONLY = re.compile(r"\[cite:\s*(.+?)\]", re.S)
RE_CITE_ONLY_BARE = re.compile(r"\[cite\]")
# [12, 34] or [12, 34; cite: something]
RE_NUMCITE = re.compile(
    rf"\[\s*({CITE_KEYS}(?:\s*,\s*{CITE_KEYS})*)\s*(?:;\s*(cite:\s*.+?))?\s*\]", re.S
)
RE_BOLD = re.compile(r"\*\*(.+?)\*\*", re.S)
RE_ITAL_U = re.compile(r"(?<![A-Za-z0-9\\])_(?!_)(.+?)(?<!_)_(?![A-Za-z0-9])", re.S)
RE_ITAL_A = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", re.S)
RE_CODE = re.compile(r"`([^`]+)`")
RE_MDLINK = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")


def inline(text: str, vault: Vault, report: dict) -> str:
    """Convert inline markdown, stashing LaTeX so escape() cannot mangle it."""

    text = RE_MDLINK.sub(lambda m: vault.stash(r"\href{%s}{%s}" % (m.group(2), inline(m.group(1), vault, report))), text)

    def missing(m: re.Match) -> str:
        report["missing_data"].append(m.group(1).strip())
        return vault.stash(r"\suggestion{[MISSING DATA: %s]}" % escape(m.group(1).strip()))

    text = RE_MISSING.sub(missing, text)

    def citeonly(m: re.Match) -> str:
        report["cite_placeholders"].append(m.group(1).strip())
        return vault.stash(r"\suggestion{[cite: %s]}" % escape(m.group(1).strip()))

    text = RE_CITE_ONLY.sub(citeonly, text)

    def citebare(m: re.Match) -> str:
        report["cite_placeholders"].append("(unspecified)")
        return vault.stash(r"\suggestion{[cite]}")

    text = RE_CITE_ONLY_BARE.sub(citebare, text)

    def numcite(m: re.Match) -> str:
        keys = [k.strip() for k in m.group(1).split(",") if k.strip()]
        # A bracket whose contents are not plausible bib keys is prose, not a citation.
        if not all(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_:\-\.\+]*", k) for k in keys):
            return m.group(0)
        if any(k.lower() in {"cite", "missing", "todo"} for k in keys):
            return m.group(0)
        report["cites"].extend(keys)
        out = r"\cite{%s}" % ",".join(keys)
        if m.group(2):
            note = m.group(2).strip()
            report["cite_placeholders"].append(note)
            out += r"\suggestion{[%s]}" % escape(note)
        return vault.stash(out)

    text = RE_NUMCITE.sub(numcite, text)

    text = RE_CODE.sub(lambda m: vault.stash(r"\texttt{%s}" % escape(m.group(1))), text)
    text = RE_BOLD.sub(lambda m: vault.stash(r"\textbf{%s}" % inline(m.group(1), vault, report)), text)
    text = RE_ITAL_U.sub(lambda m: vault.stash(r"\textit{%s}" % inline(m.group(1), vault, report)), text)
    text = RE_ITAL_A.sub(lambda m: vault.stash(r"\textit{%s}" % inline(m.group(1), vault, report)), text)

    text = escape(text)

    # quotes: opening " when preceded by start/space/open bracket
    text = re.sub(r'(^|[\s(\[])"', r"\1``", text)
    text = text.replace('"', "''")
    text = re.sub(r"(^|[\s(\[])'", r"\1`", text)

    return text


# ---------------------------------------------------------------- block rules

RE_H = re.compile(r"^(#{1,6})\s+(.*)$")
RE_UL = re.compile(r"^\s*[-*+]\s+(.*)$")
RE_OL = re.compile(r"^\s*\d+[.)]\s+(.*)$")
RE_BQ = re.compile(r"^\s*>\s?(.*)$")
RE_HR = re.compile(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$")
RE_TABLE = re.compile(r"^\s*\|.*\|\s*$")

HEAD_CMD = {2: "subsection", 3: "subsubsection", 4: "paragraph", 5: "paragraph", 6: "paragraph"}


def convert(md: str, section_title: str | None, emit_section: bool) -> tuple[str, dict]:
    report = {
        "cites": [],
        "cite_placeholders": [],
        "missing_data": [],
        "dashes": [],
        "tables": 0,
        "warnings": [],
    }
    vault = Vault()

    md = normalize(md)
    # strip YAML frontmatter
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)

    for n, line in enumerate(md.splitlines(), 1):
        if "--" in line and not RE_HR.match(line) and not RE_TABLE.match(line.strip()):
            for m in re.finditer(r"\S*-{2,3}\S*", line):
                report["dashes"].append({"line": n, "text": m.group(0)})

    lines = md.splitlines()
    out: list[str] = []
    i = 0
    seen_h1 = False
    list_stack: list[str] = []

    def close_lists() -> None:
        while list_stack:
            out.append(r"\end{%s}" % list_stack.pop())

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            close_lists()
            if out and out[-1] != "":
                out.append("")
            i += 1
            continue

        if RE_HR.match(stripped):
            i += 1
            continue

        m = RE_H.match(stripped)
        if m:
            close_lists()
            level, title = len(m.group(1)), m.group(2).strip().rstrip("#").strip()
            title_tex = inline(title, vault, report)
            if level == 1:
                seen_h1 = True
                if emit_section:
                    name = escape(section_title) if section_title else title_tex
                    out += ["", r"\section{%s}" % name, ""]
            else:
                out += ["", r"\%s{%s}" % (HEAD_CMD[level], title_tex), ""]
            i += 1
            continue

        if RE_TABLE.match(stripped):
            block = []
            while i < len(lines) and RE_TABLE.match(lines[i].strip()):
                block.append(lines[i].strip())
                i += 1
            report["tables"] += 1
            out += ["", r"%% TODO(/latex): markdown table below needs a hand-built"
                    r" tabular/table environment with caption and label.", ""]
            for b in block:
                out.append("% " + b)
            out.append("")
            continue

        m = RE_BQ.match(line)
        if m:
            close_lists()
            body = []
            while i < len(lines) and RE_BQ.match(lines[i]):
                body.append(RE_BQ.match(lines[i]).group(1).strip())
                i += 1
            out += ["", r"\begin{itquote}", inline(" ".join(body).strip(), vault, report),
                    r"\end{itquote}", ""]
            continue

        m = RE_UL.match(line)
        if m:
            if not list_stack or list_stack[-1] != "itemize":
                close_lists()
                out.append(r"\begin{itemize}")
                list_stack.append("itemize")
            out.append(r"  \item " + inline(m.group(1).strip(), vault, report))
            i += 1
            continue

        m = RE_OL.match(line)
        if m:
            if not list_stack or list_stack[-1] != "enumerate":
                close_lists()
                out.append(r"\begin{enumerate}")
                list_stack.append("enumerate")
            out.append(r"  \item " + inline(m.group(1).strip(), vault, report))
            i += 1
            continue

        # paragraph: gather until blank line or a block marker
        para = []
        while i < len(lines):
            cur = lines[i]
            if (not cur.strip()) or RE_H.match(cur.strip()) or RE_UL.match(cur) \
               or RE_OL.match(cur) or RE_BQ.match(cur) or RE_HR.match(cur.strip()) \
               or RE_TABLE.match(cur.strip()):
                break
            para.append(cur.strip())
            i += 1
        close_lists()
        out.append(inline(" ".join(para), vault, report))
        out.append("")

    close_lists()

    if emit_section and not seen_h1 and section_title:
        out = ["", r"\section{%s}" % escape(section_title), ""] + out

    tex = "\n".join(out)
    tex = vault.restore(tex)
    tex = re.sub(r"\n{3,}", "\n\n", tex).strip() + "\n"

    report["cites"] = sorted(set(report["cites"]), key=lambda k: (not k.isdigit(), int(k) if k.isdigit() else k))
    return tex, report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--out")
    ap.add_argument("--section-title")
    ap.add_argument("--no-section", action="store_true")
    ap.add_argument("--report")
    a = ap.parse_args()

    md = Path(a.input).read_text(encoding="utf-8")
    tex, report = convert(md, a.section_title, not a.no_section)

    if a.out:
        Path(a.out).write_text(tex, encoding="utf-8")
    else:
        sys.stdout.write(tex)

    report["input"] = a.input
    report["output"] = a.out or "(stdout)"
    if a.report:
        Path(a.report).write_text(json.dumps(report, indent=2), encoding="utf-8")
    else:
        sys.stderr.write(json.dumps(report, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
