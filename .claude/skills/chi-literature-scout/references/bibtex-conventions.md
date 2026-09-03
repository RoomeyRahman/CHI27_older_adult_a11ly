# BibTeX conventions for HCI venues

## Citation keys
`firstauthorYEARkeyword`, all lowercase: `ahmed2021proxy`, `pater2019standardizing`.
Never reuse a key. When two papers collide, extend the keyword: `ahmed2021proxycare`.

## Entry types by venue

| Venue | Entry type | Notes |
|---|---|---|
| CHI (all years) | `@inproceedings` | booktitle = {Proceedings of the CHI Conference on Human Factors in Computing Systems} |
| CSCW 2017 and earlier | `@inproceedings` | |
| CSCW 2018+ | `@article` | journal = {Proceedings of the ACM on Human-Computer Interaction}, include `number = {CSCW...}` if known |
| IMWUT / UbiComp 2017+ | `@article` | journal = {Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.} |
| DIS, UIST, ASSETS, FAccT, IDC | `@inproceedings` | |
| TOCHI | `@article` | journal = {ACM Transactions on Computer-Human Interaction} |
| ACL/EMNLP/NAACL | `@inproceedings` | |
| arXiv preprints | `@misc` | include `eprint`, `archivePrefix = {arXiv}`, and mark year; prefer the published version if one exists |

## Template

```bibtex
@inproceedings{sultana2019example,
  author    = {Sultana, Sharifa and Ahmed, Syed Ishtiaque},
  title     = {Example Title in Title Case},
  booktitle = {Proceedings of the CHI Conference on Human Factors in Computing Systems},
  series    = {CHI '19},
  year      = {2019},
  publisher = {ACM},
  address   = {New York, NY, USA},
  doi       = {10.1145/XXXXXXX.XXXXXXX}
}
```

## Rules
- Omit fields you could not verify; never guess page numbers or DOIs.
- Protect acronyms and proper nouns in titles with braces: `{AI}`, `{Bangladesh}`, `{HCI4D}`.
- Author names: `Last, First and Last, First`. Up to ~10 authors, then `and others`.
- Group entries under `% ==== Stream: <name> ====` comment banners matching the literature map.
- De-duplicate by DOI first, then by normalized title.
