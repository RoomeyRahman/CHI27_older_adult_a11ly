<!-- slot: A1 | unit: phase1/P12 | pass: A complete | B complete | C complete | D complete | E complete -->
# P12, Phase 1: Pass B code register

## Trim rationale

Candidates after Pass A: 46. After reconciliation (23 merges): 23. Retained: 22. Parked: 1.

At the lower edge of target; the transcript is medium length and the app block is long but repetitive. Parking fell on two instrument confirmations. Frequency was not used.

Hardest calls. (1) `Alarm ignored, family voice obeyed` against `Question resolves either way`: both concern the family's asking; kept separate, because one compares person to alarm and the other names what the question does, and both mechanisms matter. (2) `Keeps phone charged for alarm` is a single line; retained, because it is the only place in the phase where the maintenance of a technology falls on the older adult and is described as routine.

## Merges (old names kept)

- `Alarm set at midnight` + `Alarm set once, rings daily` + `Midnight dose` + `Alarm only, no app` → **Alarm set once, rings daily**.
- `Hears alarm, defers, forgets` + `Alarm helps, not enough` + `Absorbed: talking, watching` → **Hears alarm, defers, forgets**.
- `Travel: forgets where in the bag` + `Carries but misses the time` + `Busy or travelling is hardest` → **Carries but misses the time**.
- `One medicine, at home` + `One medicine, no confusion` + `One place at home` → **One place at home**.
- `Family asks sometimes` + `Husband or whoever, not daily` → **Husband or whoever, not daily**.
- `Others taking cues her` + `'seeing them reminds me' [tr]` → **Others taking cues her**.
- `Consensus noted, still asks` + `Group matters, doctor or pharmacist gates` + `Many voices over one` → **Group matters, doctor or pharmacist gates**.
- `Pharmacy reads the prescription` + `'We cannot understand properly' [tr]` → **Pharmacy reads the prescription**.
- `Phone reading would help` + `Prescription reading welcome` + `Picture against similar packets` → **Prescription reading welcome**.
- `Name, time, count; no more` + `Basic information only` + `Reminder and information both` → **Name, time, count; no more**.
- `Doctor for problems, pharmacist small` + `Doctor for medicine, pharmacy for name` + `Doctor's number in her phone` → **Doctor for medicine, pharmacy for name**.
- `Wants a strong voice reminder` + `'There are many notifications' [tr]` + `Voice reminder and reading, that's all` → **'There are many notifications' [tr]**.
- `Too many steps for one medicine` + `'Open and see. Or just tell me' [tr]` → **'Open and see. Or just tell me' [tr]**.

## Register

| Code | Status | RQ | Mech | Corr | Grade | Load | Practice | Reason |
|---|---|---|---|---|---|---|---|---|
| One medicine, at home | MERGED | | | | | | | Into One place at home |
| Midnight dose | MERGED | | | | | | | Into Alarm set once, rings daily |
| Alarm set at midnight | MERGED | | | | | | | Into Alarm set once, rings daily |
| Alarm set once, rings daily | RETAINED | 1 | yes | L13, L17, L97 | V | The only existing medicine technology; standing configuration | | Baseline for the account |
| Hears alarm, defers, forgets | RETAINED | 1 | yes | L29, L33 | V | The alarm reminds; absorption defers past it | | Mechanism of the alarm's limit |
| Alarm helps, not enough | MERGED | | | | | | | Into Hears alarm, defers, forgets |
| Absorbed: talking, watching | MERGED | | | | | | | Into Hears alarm, defers, forgets |
| Travel: forgets where in the bag | MERGED | | | | | | | Into Carries but misses the time |
| Carries but misses the time | RETAINED | 1 | yes | L37, L149 | V | Travel lapses: carrying does not secure timing; loses it in the bag | | Distinct from home lapses |
| One medicine, no confusion | MERGED | | | | | | | Into One place at home |
| One place at home | RETAINED | 1 | yes | L5, L45 | V | Spatial anchoring; one medicine | | Same as other accounts |
| Family asks sometimes | MERGED | | | | | | | Into Husband or whoever, not daily |
| Husband or whoever, not daily | RETAINED | 1 | yes | L53 | V | Unassigned, intermittent asking | | Network shape |
| Question resolves either way | RETAINED | 1 | yes | none | V | The question checks without presuming a lapse | | Mechanism, stated exactly |
| Alarm ignored, family voice obeyed | RETAINED | 1 | yes | none | V (form E) | The person outranks the alarm | | The account's contribution |
| Others taking cues her | RETAINED | 1 | yes | L73 | V | Peer cue at gatherings | | Same as P04, P05 |
| 'seeing them reminds me' [tr] | MERGED | | | | | | | Into Others taking cues her |
| Consensus noted, still asks | MERGED | | | | | | | Into Group matters, doctor or pharmacist gates |
| Group matters, doctor or pharmacist gates | RETAINED | 1 | yes | L77, L85 | E, H | Group opinion weighed; the doctor or pharmacist gates | | Same boundary; probed |
| Many voices over one | MERGED | | | | | | | Into Group matters, doctor or pharmacist gates |
| Other household tablets confuse | RETAINED | 1 | yes | none | V | Others' medicines in the house as the confusion source | | Household-specific mechanism |
| Alarm only, no app | MERGED | | | | | | | Into Alarm set once, rings daily |
| Family familiar with phones | PARKED | none | no | L105 | E | Inventory | | Household competence carried by the help code |
| Family helps with new things | RETAINED | 1 | yes | L101 | V | Help for novelty only; normal use is theirs | | Bounded delegation |
| Pharmacy reads the prescription | RETAINED | 1 | yes | L113 | V | Third-party reading; plural 'we' | assignment | Same as other accounts |
| 'We cannot understand properly' [tr] | MERGED | | | | | | | Into Pharmacy reads the prescription |
| Phone reading would help | MERGED | | | | | | | Into Prescription reading welcome |
| Name, time, count; no more | RETAINED | 3 | yes | L173, L177 | H | The information she wants, bounded | | Instrument-adjacent but recurs |
| Picture against similar packets | MERGED | | | | | | | Into Prescription reading welcome |
| Doctor for problems, pharmacist small | MERGED | | | | | | | Into Doctor for medicine, pharmacy for name |
| Doctor for medicine, pharmacy for name | RETAINED | 1 | yes | L133, L141 | V | Precise division of clinical contact; number self-held | | Her own division |
| Doctor's number in her phone | MERGED | | | | | | | Into Doctor for medicine, pharmacy for name |
| Busy or travelling is hardest | MERGED | | | | | | | Into Carries but misses the time |
| Wants a strong voice reminder | MERGED | | | | | | | Into 'There are many notifications' [tr] |
| 'There are many notifications' [tr] | RETAINED | 3 | yes | L153, L217 | H | Voice preferred because text competes with clutter | | The agent contends for attention |
| Repeat after minutes, not constantly | RETAINED | 3 | yes | none | E, H | Bounded repetition; constant repeats irritate | | Condition on the agent's persistence |
| One family member may know | RETAINED | 2, 3 | yes | none | E, H | Family notification accepted, one member | assignment | Elicited but specific |
| Not monitored if it is family | RETAINED | 2 | yes | L53, L65 | E (frame) | Monitoring redefined by the identity of the asker | | Frame offered; reason hers |
| Reminder and information both | MERGED | | | | | | | Into Name, time, count; no more |
| Basic information only | MERGED | | | | | | | Into Name, time, count; no more |
| Prescription reading welcome | RETAINED | 3 | yes | L121, L129 | E, H | Reading and pictures welcome | | Recurs, elicited |
| Keeps phone charged for alarm | RETAINED | 1 | yes | none | V | Maintenance of the technology as her routine responsibility | | Only such statement in the phase |
| Too many steps for one medicine | MERGED | | | | | | | Into 'Open and see. Or just tell me' [tr] |
| 'Open and see. Or just tell me' [tr] | RETAINED | 3 | yes | L201 | E | Simplicity condition in her words | | In-vivo |
| Travel reminder wanted | RETAINED | 3 | yes | L37, L149 | H | A want tied to her named lapse | | Volunteered |
| Voice reminder and reading, that's all | MERGED | | | | | | | Into 'There are many notifications' [tr] |

Retained: 22. Parked: 1. Merged: 23. Total accounted: 46.
