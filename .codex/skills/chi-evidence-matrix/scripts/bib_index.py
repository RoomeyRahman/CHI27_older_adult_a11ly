#!/usr/bin/env python3
"""Parse a .bib file into a citation-key index and match entries to PDF files.

Usage:
    python bib_index.py refs.bib --papers ./pdfs --out work/bib_index.json

Produces bib_index.json:
    {"entries": {"smith2021trust": {"key":..., "type":..., "authors":..., "year":...,
                                    "title":..., "venue":..., "doi":...,
                                    "matched_file": "smith_chi21.pdf",
                                    "match_confidence": "high"}},
     "unmatched_pdfs": [...], "unmatched_entries": [...]}

Citation keys in the output tables must come from this file. Nothing else is
authoritative -- keys written from memory are how fabricated references happen.
"""

import argparse
import json
import re
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

FIELDS = ("author", "year", "title", "booktitle", "journal", "publisher",
          "doi", "series", "url")
STOP = {"the", "a", "an", "of", "for", "and", "in", "on", "to", "with", "at",
        "from", "by", "via", "using", "towards", "toward"}


def strip_braces(s):
    s = s.strip()
    while s and s[0] in "{\"" and s[-1] in "}\"":
        s = s[1:-1].strip()
    return re.sub(r"\s+", " ", s.replace("{", "").replace("}", "")).strip()


def parse_bib(text):
    """Brace-balanced parse. Tolerant of comments, @string, and trailing commas."""
    entries = []
    i = 0
    while True:
        at = text.find("@", i)
        if at == -1:
            break
        m = re.match(r"@(\w+)\s*[{(]", text[at:])
        if not m:
            i = at + 1
            continue
        etype = m.group(1).lower()
        start = at + m.end()
        if etype in ("comment", "string", "preamble"):
            i = start
            continue
        depth, j = 1, start
        while j < len(text) and depth:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        body = text[start:j - 1]
        i = j

        key, _, rest = body.partition(",")
        entry = {"key": key.strip(), "type": etype}
        # split fields at top-level commas only
        depth, buf, parts = 0, [], []
        for ch in rest:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            if ch == "," and depth == 0:
                parts.append("".join(buf))
                buf = []
            else:
                buf.append(ch)
        parts.append("".join(buf))
        for part in parts:
            if "=" not in part:
                continue
            name, _, val = part.partition("=")
            name = name.strip().lower()
            if name in FIELDS:
                entry[name] = strip_braces(val)
        entries.append(entry)
    return entries


def normalize(entry):
    year = re.sub(r"\D", "", entry.get("year", ""))[:4] or "Not reported"
    venue = entry.get("booktitle") or entry.get("journal") or entry.get("series") \
        or entry.get("publisher") or "Not reported"
    return {
        "key": entry["key"],
        "type": entry["type"],
        "authors": entry.get("author", "Not reported"),
        "year": year,
        "title": entry.get("title", "Not reported"),
        "venue": venue,
        "doi": entry.get("doi", "Not reported"),
    }


def slug(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]", " ", s)


def tokens(s):
    return [w for w in slug(s).split() if w not in STOP and len(w) > 2]


def score(entry, filename):
    fname = slug(Path(filename).stem)
    ftok = set(tokens(fname))
    ttok = tokens(entry["title"])
    if not ttok:
        return 0.0
    overlap = len(ftok & set(ttok)) / len(set(ttok))
    seq = SequenceMatcher(None, fname, slug(entry["title"])[:len(fname) + 20]).ratio()
    surname = slug(entry["authors"].split(",")[0].split(" and ")[0]).split()
    surname = surname[-1] if surname else ""
    bonus = 0.0
    if surname and surname in fname:
        bonus += 0.35
    if entry["year"] != "Not reported" and entry["year"][-2:] in fname:
        bonus += 0.15
    return min(1.0, max(overlap, seq) + bonus)


def match(entries, papers_dir):
    pdfs = []
    p = Path(papers_dir)
    if p.is_file():
        pdfs = [p]
    elif p.is_dir():
        pdfs = sorted(x for x in p.rglob("*") if x.suffix.lower() in (".pdf", ".txt", ".md"))
    used = set()
    for e in entries:
        best, best_s = None, 0.0
        for f in pdfs:
            if f.name in used:
                continue
            s = score(e, f.name)
            if s > best_s:
                best, best_s = f, s
        if best and best_s >= 0.45:
            e["matched_file"] = best.name
            e["match_confidence"] = "high" if best_s >= 0.7 else "low — verify against title page"
            used.add(best.name)
        else:
            e["matched_file"] = None
            e["match_confidence"] = "none"
    unmatched_pdfs = [f.name for f in pdfs if f.name not in used]
    return unmatched_pdfs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bib")
    ap.add_argument("--papers", default=None)
    ap.add_argument("--out", default="bib_index.json")
    args = ap.parse_args()

    raw = Path(args.bib).read_text(encoding="utf-8", errors="replace")
    entries = [normalize(e) for e in parse_bib(raw) if e.get("key")]
    if not entries:
        raise SystemExit(f"No entries parsed from {args.bib} — check the file.")

    dupes = [k for k in {e["key"] for e in entries}
             if sum(1 for e in entries if e["key"] == k) > 1]

    unmatched_pdfs = match(entries, args.papers) if args.papers else []
    unmatched_entries = [e["key"] for e in entries if not e.get("matched_file")]

    out = {
        "entries": {e["key"]: e for e in entries},
        "unmatched_pdfs": unmatched_pdfs,
        "unmatched_entries": unmatched_entries,
        "duplicate_keys": dupes,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2), encoding="utf-8")

    low = [e["key"] for e in entries if e.get("match_confidence", "").startswith("low")]
    print(f"parsed {len(entries)} bib entries -> {args.out}")
    print(f"matched to files: {len(entries) - len(unmatched_entries)}")
    if low:
        print(f"low-confidence matches (verify title page): {', '.join(low[:10])}")
    if unmatched_pdfs:
        print(f"PDFs with no bib entry ({len(unmatched_pdfs)}): {', '.join(unmatched_pdfs[:10])}")
    if unmatched_entries:
        print(f"bib entries with no PDF ({len(unmatched_entries)}): {', '.join(unmatched_entries[:10])}")
    if dupes:
        print(f"DUPLICATE KEYS: {', '.join(dupes)}")


if __name__ == "__main__":
    main()
