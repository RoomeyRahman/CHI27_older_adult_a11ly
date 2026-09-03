#!/usr/bin/env python3
"""Verify that every attributed extract in /output/codes/ appears verbatim in its source transcript.

Catches the failure mode the multi-pass protocol exists to prevent: a quote recalled while writing a
theme rather than read from the data, or a quote silently tidied for readability.

Usage:  python3 .claude/skills/thematic-analysis/scripts/quote_check.py [repo_root] [slot]

`slot` (A1, A2, ...) restricts the scan to /output/codes/<slot>/, which is what an agent sharing the
repository with another agent's analysis should use. Omit it to scan everything under /output/codes/.

Exit 0 = every extract found. Exit 1 = at least one extract not found verbatim. Exit 2 = paths missing.

Matching rules:
  * curly quotes, dashes, and runs of whitespace are normalised before comparison
  * an elision [...] splits the extract into fragments, each of which must be found, in order
  * a bracketed insertion [like this] is treated as a wildcard and not required to be present
  * fragments shorter than 12 characters after normalisation are skipped as unmatchable
"""

import os
import re
import sys
import unicodedata

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
SLOT = sys.argv[2].upper() if len(sys.argv) > 2 else ""
OUT = os.path.join(ROOT, "output", "codes", SLOT) if SLOT else os.path.join(ROOT, "output", "codes")
# One directory per study. A transcript file is named for the participant id it carries, so
# supplementary/formative/OA03.md is participant OA03 and supplementary/household/H2-CG1.md is H2-CG1.
STUDY_DIRS = [
    os.path.join(ROOT, "supplementary", "formative"),    # Study 1
    os.path.join(ROOT, "supplementary", "deployment"),   # Study 2
    os.path.join(ROOT, "supplementary", "household"),    # Study 3
]

# OA01..OA17 older adults and CG01..CG09 caregivers in Study 1; D1..D6 in Study 2;
# H1-OA, H1-CG1 and so on in Study 3.
PID = r"OA\d+|CG\d+|D\d+|H\d+(?:-(?:OA|CG\d*))?"

MIN_FRAGMENT = 12


def normalise(text):
    text = unicodedata.normalize("NFKC", text)
    for a, b in [("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("…", "...")]:
        text = text.replace(a, b)
    text = re.sub(r"[*_`\\]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def load_sources():
    """Map participant id -> normalised transcript text, across every study directory."""
    src = {}
    for study_dir in STUDY_DIRS:
        if not os.path.isdir(study_dir):
            continue
        for dirpath, _dirs, files in os.walk(study_dir):
            for name in files:
                m = re.fullmatch(r"(" + PID + r")\.md", name, re.IGNORECASE)
                if not m:
                    continue
                with open(os.path.join(dirpath, name), encoding="utf-8", errors="replace") as fh:
                    src[m.group(1).upper()] = normalise(fh.read())
    return src


# "extract text" (OA03, 04:44)   |   "extract text" (D5)   |   "extract text" (H2-CG1)
QUOTED = re.compile(r'"([^"\n]{10,})"[^()\n]{0,80}?\(\s*(' + PID + r')\s*[^)]*\)', re.IGNORECASE)
# > block quote line ... (OA03, 14:04)
BLOCKQ = re.compile(r'^>+\s*"?(.+?)"?\s*\(\s*(' + PID + r')\s*[^)]*\)\s*$', re.MULTILINE | re.IGNORECASE)


def fragments(extract):
    parts = re.split(r"\[\s*(?:\.\.\.|…)\s*\]", extract)
    out = []
    for part in parts:
        part = re.sub(r"\[[^\]]*\]", " ", part)  # insertions and tags act as wildcards
        part = normalise(part)
        if len(part) >= MIN_FRAGMENT:
            out.append(part)
    return out


def main():
    if not os.path.isdir(OUT):
        print("MISSING: %s (nothing written yet)" % OUT)
        return 2
    sources = load_sources()
    if not sources:
        print("MISSING: no transcripts found under %s" % ", ".join(STUDY_DIRS))
        return 2

    checked = skipped = 0
    failures = []

    for dirpath, _dirs, files in os.walk(OUT):
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            for line_no, raw in enumerate(text.splitlines(), 1):
                for pattern in (QUOTED, BLOCKQ):
                    for m in pattern.finditer(raw):
                        extract, pid = m.group(1), m.group(2).upper()
                        key = pid
                        if key not in sources:
                            failures.append((path, line_no, pid, extract,
                                             "no source transcript for %s" % pid))
                            continue
                        frags = fragments(extract)
                        if not frags:
                            skipped += 1
                            continue
                        checked += 1
                        hay = sources[key]
                        cursor = 0
                        for frag in frags:
                            idx = hay.find(frag, cursor)
                            if idx < 0:
                                failures.append((path, line_no, pid, frag,
                                                 "fragment not found verbatim in source"))
                                break
                            cursor = idx + len(frag)

    rel = lambda p: os.path.relpath(p, ROOT)
    print("Extracts checked: %d   (fragments too short to check: %d)" % (checked, skipped))
    if failures:
        print("FAIL: %d extract(s) could not be verified" % len(failures))
        print("---")
        for path, line_no, pid, frag, why in failures:
            snippet = frag if len(frag) <= 110 else frag[:107] + "..."
            print("%s:%d  [%s]  %s" % (rel(path), line_no, pid, why))
            print("    %s" % snippet)
        print("---")
        print("Either the extract was altered, or it is attributed to the wrong participant, or it")
        print("was not read from the transcript at all. Fix it in the source of truth, the transcript,")
        print("never by editing the quote to match what was written.")
        return 1
    print("PASS: every attributed extract found verbatim in its source transcript")
    return 0


if __name__ == "__main__":
    sys.exit(main())
