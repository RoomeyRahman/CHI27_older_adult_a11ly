#!/usr/bin/env bash
# Anonymization scan for /output/codes/.
#
# Derives candidate personal names from the source transcripts at run time (so no real name is ever
# stored in this repository's skill files), then checks whether any of them appear in the analysis
# output. Also reports Title Case bigrams in the output that are not on the allowlist, which catches
# names the derivation missed.
#
# Usage:  bash .codex/skills/thematic-analysis/scripts/anon_scan.sh [repo_root] [slot]
#
# `slot` (A1, A2, ...) restricts the scan to output/codes/<slot>/. Omit it to scan every slot.
# Exit 0 = clean. Exit 1 = a candidate name was found in /output/codes/. Exit 2 = paths missing.

set -uo pipefail
ROOT="${1:-$(pwd)}"
SLOT="$(printf '%s' "${2:-}" | tr '[:lower:]' '[:upper:]')"
SRC="$ROOT/supplementary"
if [ -n "$SLOT" ]; then OUT="$ROOT/output/codes/$SLOT"; else OUT="$ROOT/output/codes"; fi

[ -d "$SRC" ] || { echo "MISSING: $SRC"; exit 2; }
[ -d "$OUT" ] || { echo "MISSING: $OUT (nothing written yet)"; exit 2; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Words that look like names but are roles, places, brands, institutions, or study vocabulary.
# Extend this list rather than weakening the pattern.
cat > "$TMP/stop.txt" <<'STOP'
Participant Interviewer Facilitator Researcher Candidate Speaker Moderator
Onboarding Session Interview Duration Approximately Question Questions Consent Form
Bangla Bangladesh Bengali English Hindi Dhaka Bangladeshi
ChatGPT WhatsApp Facebook Messenger Imo Viber YouTube Google OpenAI Anthropic Claude
Alexa Siri Android Nokia Symphony Walton Samsung Xiaomi Realme
Chittagong Chattogram Sylhet Khulna Rajshahi Barisal Rangpur Mymensingh Comilla Gazipur
Metformin Insulin Losartan Amlodipine Napa Seclo Omeprazole Paracetamol Glimepiride
Diabetes Hypertension Pressure Sugar Blood Eye Cataract Stroke Kidney Heart
Doctor Pharmacist Pharmacy Hospital Clinic Prescription Medicine Medication Dose Doses
Association Community Network Support Group Family Household Care Caregiver Ledger
Affiliation Allegiance Ceremony Revocation Gifting Contestation Assignment Advocate Coach Tool
Streak Streaks Score Scores Points Reminder Reminders Notification Probationary
Assalamu Alaikum Walaikum Salam Wa Insha Allah Alhamdulillah
Yes No Right Okay Thank Thanks Hello Sorry Actually
The That This What When Where Which While With Would Could Should Since Then There
And But For From Have How Only Some Such They Their Them Very Was Were You Your
Also About After Because Before Being Both Does Each Even Every First Just Like
Made Make More Most Much Must Need Now One Other Over Same Says Said Take Than
Video Videos Tool Tools Speech Content People Person Time Times
Older Adult Adults Elder Elderly Son Daughter Mother Father Wife Husband Sister Brother
Morning Night Evening Afternoon Breakfast Lunch Dinner Meal Wedding Travel Traffic
Code Codes Theme Themes Sub Note Notes Phase Table Matrix Report Analysis Analytic
Example Quotes Quote Definition Reflexivity Extract Extracts Codebook Memo
Absolutely Almost Another Any Are Check Not Nowadays Sometimes Using Usually
Text Thinking Negative Positive Reading Writing Editing Speaking Listening Manual Once Those Whole Keep While Where Until Suppose Anything Everything Nothing Somebody
Basically Certainly Currently Definitely Earlier Everyone Exactly Firstly Generally
Due During Looking Maintaining Ensuring Regarding Toward Towards Against Alongside Can May Might Will Shall
Honestly However Imagine Initially Maybe Nothing Obviously Personally Possibly
Previously Probably Rather Really Recently Someone Something Suppose Sure Therefore
Though Today Together Usually Whether Yeah Yesterday
Who Whom Whose Why Who's Nobody Anyone Everybody Neither Either
STOP

# 1. Candidate names from the transcripts, taken from name-bearing positions only:
#    speaker labels, header rows, and bold name lines. Broad Title Case matching produces
#    too many sentence-start false positives to be usable as a gate.
{
  # "Participant: Some Name", "Interviewer: Some Name", "Facilitator - Some Name"
  grep -hoE '(Participant|Interviewer|Facilitator|Candidate|Moderator)[*:| ]{1,6}[A-Z][a-z]+( [A-Z][a-z]+){0,3}' -r "$SRC" 2>/dev/null \
    | sed -E 's/^(Participant|Interviewer|Facilitator|Candidate|Moderator)[*:| ]*//'
  # "Participant (Some Name)"
  grep -hoE '(Participant|Interviewer|Facilitator)[^()]{0,12}\([A-Z][a-z]+( [A-Z][a-z]+){0,3}\)' -r "$SRC" 2>/dev/null \
    | grep -oE '\([A-Z][a-z]+( [A-Z][a-z]+){0,3}\)' | tr -d '()'
  # Table cells: "| Some Name |"
  grep -hoE '\| *[A-Z][a-z]+( [A-Z][a-z]+){1,3} *\|' -r "$SRC" 2>/dev/null | tr -d '|'
  # Bold standalone name lines: "**Some Name**"
  grep -hoE '^\*\*[A-Z][A-Za-z]+( [A-Z][a-z]+){1,3}\*\*$' -r "$SRC" 2>/dev/null | tr -d '*'
} | sed -E 's/^ +| +$//g' | sed '/^$/d' | sort -u > "$TMP/cand_multi.txt"

# Component tokens too, so a first name used alone is still caught.
tr ' ' '\n' < "$TMP/cand_multi.txt" | sed '/^$/d' | sort -u > "$TMP/cand_single.txt"

# Remove stopwords.
tr ' ' '\n' < "$TMP/stop.txt" | sed '/^$/d' | sort -u > "$TMP/stop_tokens.txt"
comm -23 <(sort -u "$TMP/cand_single.txt") "$TMP/stop_tokens.txt" > "$TMP/names.txt"
# A multi-word candidate composed entirely of stoplisted tokens is by construction not a name.
while IFS= read -r line; do
  keep=0
  for w in $line; do
    grep -qxF "$w" "$TMP/stop_tokens.txt" || keep=1
  done
  [ "$keep" -eq 1 ] && echo "$line"
done < "$TMP/cand_multi.txt" >> "$TMP/names.txt"
sort -u "$TMP/names.txt" | sed '/^.\{0,2\}$/d' > "$TMP/names_final.txt"

echo "Candidate personal-name tokens derived from source: $(wc -l < "$TMP/names_final.txt" | tr -d ' ')"

# 3. Scan the analysis output for any of them.
HITS="$TMP/hits.txt"
: > "$HITS"
while IFS= read -r n; do
  grep -rnwF -- "$n" "$OUT" 2>/dev/null | sed "s/^/[$n] /" >> "$HITS"
done < "$TMP/names_final.txt"

if [ -s "$HITS" ]; then
  echo "FAIL: candidate real names found in $OUT"
  echo "---"
  cat "$HITS"
  echo "---"
  echo "Replace each with its participant id (OA01..OA17, CG01..CG09, D1..D6, H1-OA, H1-CG1),"
  echo "[Interviewer], [Facilitator], or a"
  echo "bracketed generic ([a psychiatrist], [a university]), then re-run."
  exit 1
fi

echo "PASS: no derived source name appears in $OUT"

# 4. Residual check: Title Case bigrams in the output that are not obviously safe.
echo
echo "Residual Title Case bigrams in output (review by eye; most will be legitimate):"
grep -rhoE '\b[A-Z][a-z]{2,} [A-Z][a-z]{2,}\b' "$OUT" 2>/dev/null \
  | grep -vxFf "$TMP/stop.txt" 2>/dev/null \
  | sort | uniq -c | sort -rn | head -30

exit 0
