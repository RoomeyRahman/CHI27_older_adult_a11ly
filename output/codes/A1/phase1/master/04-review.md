<!-- slot: A1 | unit: phase1/master | pass: A complete | B complete | C complete | D complete | E complete -->
# Phase 1 master synthesis: Pass E review

## Chain walks

Downward: MT1 to S1, S3, S4 to 11 master codes to 176 constituent per-unit codes to extracts; MT2 to S2, S5, S7 to 10 codes to 131 constituents; MT3 to S6, S8 and the three reception codes to 6 codes to 49 constituents; MT4 to S9 to S12 to 13 codes to 154 constituents. Every constituent per-unit code exists in its unit's register as RETAINED, and every unit matrix row is either in a master code or in the parked list at the end of `01-code-synthesis.md` (4 rows). No link failed.

Upward: eighteen extracts sampled across units (P01 L83, P02 L481, P03 L127, P04 L167, P05 L223, P06 L267, P07 L175, P08 L121, P09 L74, P10 L36, P11 L35, P12 L65, P13 L53, P15 L62, P17 L27, C01 L325, C02 L89, C03 L37). For each I asked whether the code still fits, whether the master sub-theme is where a reader would put it, and whether the theme is a claim it supports. Seventeen fit. The one contested placement is P02 L481 (`App as backstop for busy family`, in M32 under S10 in MT4): a reader might place it with M19's presence mechanism under MT2, because the backstop covers the family's absence. I left it in M32 because the extract is about the agent, and M32's definition names the family's busyness as the gap the agent fills. Hit rate 17 of 18, below the one-in-five threshold that would force Pass C to be redone.

## Mechanical checks

`quote_check.py . A1`: pass, every attributed extract found verbatim (result line in the run report). `table_check.py . A1`: pass. `anon_scan.sh . A1`: pass after extending the script's stoplist with kin address terms (Uncle, Apa, Chachi, Amma, Baba, Ma, Auntie) and common sentence-initial words (Voice, Taking, Phone, Simple, Name, Three, Second, Different, Tell, Without, Did, Walk, Coming, Finally, Meaning, Perfect, Please, Under, Suppose, Let) and speaker labels (Respondent, Woman, Person) that the derivation had picked up from interviewer turns; no real name appears in the slot.

## Counter-readings, one per theme

MT1. The alternative is that the partition is not a division that protects standing but a plain description of who can read, and I am reading dignity into literacy. It loses on the accounts of the men who can read and still distribute the work (P04's "Why to remember all", P01's sons), and on P05, a teacher, who partitions the same way. It partly holds for P08 and P09, where literacy is the stated ground; the theme's definition says the division runs by literacy and presence, and the dignity reading is in the reflexivity notes as a reading.

MT2. The alternative is that lapses are lapses of memory and the participants' locating them in occupation is a face-saving account, which the framing commitment then licenses me to accept. Three things weigh against: caregivers, who have no face to save for themselves, locate the mother's lapse the same way ("She knows she has to take it but the time goes away"); two caregivers narrate a consequential lapse as the household's inattention rather than the older adult's memory; and the false-yes mechanism is volunteered by both sides. The reading holds, and the two self-reports of decline (P07, P10) are kept inside M05 as the disconfirming cases.

MT3. The alternative is that the affirmative reception of checking and the prudence account of delegation are what older adults say to a young researcher in a house where the checker may be present, and the caregivers' "helping, not controlling" is what a caregiver says about herself. I cannot exclude this from the transcripts. Two things bound it: the irritation, scolding, and reproach in M21 were also said, so the reception is not uniformly polished; and P05's two-step account (irritated, then "she is helping") shows the repair happening in the interview rather than hidden. The theme's definition names the account as an account.

MT4. The alternative is that the design conditions are the interviewer's script reflected back. For modality preferences this is largely true and those codes were parked or merged at unit level. For the conditions retained, each exceeds its question: the record below the act (M33) was stated unprompted within a scenario by four older adults; the refusal of secret checking (M36) and the visibility of changes came with reasons; "Outside there is no one" was said by an older adult and a caregiver in different households in the same words. The reading holds for the retained set and would not for the parked one.

## Trim audit

The parked master-level rows are four: P03 `Daughter visits daily`, P08 `Box she keeps; son keeps some`, P09 `Body tells when doses lapse`, P10 `Tray, two phones, no aids observed`. With the themes finished, the one closest to the line is P09's bodily feedback, which is a cue no design supplies and which no other unit mentions; it stays parked as `[single-instance]` material available to the report, since a master code needs a second carrier or a corroborating artifact and neither exists. At unit level, the parked codes named in each unit's Pass E were re-read against the master themes; none now needs unparking, because the master codes absorbed their mechanisms under other names (for example P01's `Sons can take over` under M09, P06's `'trying to remember better now'` has no master neighbour and stays parked).

## Instrument capture

The four master themes do not reproduce the eight modules of the Phase 1 guide or the three RQs. Module 5 (technology) and module 6 (accessibility) collapsed into MT4 with their instrument codes parked; module 7 (care network) is spread across MT1, MT2, and MT3 rather than a theme of its own; module 4 (challenges) produced MT2's mechanism rather than a list of challenges. The group-opinion block, which the interviewer probed at length in most older-adult transcripts, became one master code (M16) rather than a theme, which is the correct weight for material whose salience was the instrument's.

## Participant concentration

Per theme, the largest single contributor's share of constituent per-unit codes: MT1, P06 at 8 percent; MT2, C03 at 9 percent; MT3, P07 at 16 percent; MT4, C01 at 7 percent. None approaches a third. MT3 is the most concentrated and the smallest, and P07's share is a consequence of her being the most affirmative about being checked; the theme's boundary names her position.

## Older adult against caregiver distribution

MT1: 16 older adults, 8 caregivers. MT2: 15 and 7. MT3: 13 and 3. MT4: 16 and 8. Of the 40 master codes, 27 are carried by both sides, 8 by older adults only (M02, M06, M20, M23, M27, M33 and the older-adult-only parts of M22 and M37), 3 by caregivers only (M24, M26, M36), and 2 have one side dominant. The pattern is a finding: older adults carry the competence claims, the affirmative reception of checking, the account of delegation as prudence, and the record-below-the-act condition; caregivers carry the knowledge problem in absence, the account of how the role was settled, and the visibility norm. A practice claimed by caregivers and unmentioned by older adults (M26's "it mostly just happened") is a finding about the baseline, and MT3 says so.

## Evidence grades per theme

MT1: volunteered in the main; the group-trust code (M16) is elicited. MT2: volunteered; the false-yes and the collective failures are among the most spontaneous material in the phase. MT3: mixed; the reception codes answer offered frames ("watching", "depend") but the grounds given exceed them; the role codes answer the script's specified questions. MT4: S9 and S12 reported, S10 and S11 hypothetical throughout, and the theme is labelled elicited design reasoning. No theme is all-elicited; MT4 is the one closest to being a theme about the instrument, and its retained codes were selected on exceeding the question.

## Quality checklist

Sequence
- Pass: each transcript analysed in full through all five passes before the next; the run log records the order P01 to P17, then C01 to C08.
- Pass: the master synthesis ran after all 24 units and reads registers and matrices.
- Pass: phases not merged; the cross-phase synthesis compares masters.
- Not applicable: no non-interview streams exist for this study (CLAUDE.md Section 3.5, blocker 3).
- Pending: both FINAL files, written after Phase 2 and cross-phase.

Counts
- Pass: candidates per transcript recorded; 15 of 24 units within or above the 40 to 80 range; the 9 below are short transcripts (P09 to P11, P15 to P17, C05 to C08) and the shortfall is stated in each register.
- Pass with justification: retained per transcript 25 to 30 in 12 units; 9 to 26 in the 12 short or medium units, each justified as the honest number.
- Pass: 40 master codes; 4 themes over 12 sub-themes.
- Pass: no code trimmed by frequency; every retained code carries its criteria.
- Pass: every register accounts for every candidate.

Chain of derivation
- Pass on all five items; the walks are recorded above.

Coding
- Pass: code names six words or fewer (one name at seven words, `Reminding divided by presence: co-resident asks, distant calls`, is a master name and is noted here).
- Pass: no interviewer turn quoted.
- Pass: elliptical answers recovered and tagged.
- Pass: latent layer present in every unit.
- Pass: disconfirming material retained (M05's decline self-reports, M21, M27, M40).

Themes
- Pass: each theme has one organizing concept.
- Pass: names descriptive, no subtitle, no quoted phrase, no metaphor.
- Pass: no theme is a module or an RQ restated (see instrument capture).
- Pass: every master theme clears two sources; M36 carries `[single-instance]`.
- Pass: no theme rests on one participant (see concentration).

Reporting
- Pending: prevalence, so-what, and alternative readings are checked in `FINAL-REPORT.md`.
- Pass: seeded tensions survive in the working files (M02, M05, M20, M21, M23, M27); their survival in the report is checked there.

Slot and files
- Pass: everything written inside `/output/codes/A1/`; no other slot touched.
- Pending: `README.md`, `FINAL-CODEBOOK.md`, `FINAL-REPORT.md`, written at the end of the run.
- Pass: the three scripts pass for the slot at this point.
