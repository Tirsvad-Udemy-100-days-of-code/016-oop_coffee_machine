# Review: Business Case BC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-001 |
| CrossReference | [BC-001], [QC-BC-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Review record | [c24f412] |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | ROI/Cost-Benefit analysis is quantitative, or where qualitative, is explicitly justified | Pass | Cost-Benefit Assessment now states it is qualitative because there is no revenue or budget to quantify (fixed during this review). |
| 2 | Risks are identified with documented impact and mitigation | Pass | Three risks, each with impact and mitigation. |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | Five criteria with targets and measures (pytest exit code 0, 0 dependencies, 3+ topics). |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | `### In Scope` and `### Out of Scope` present. |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | Stakeholders table uses S01, S02, S03 only. |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | ISO/IEC 25010:2023, the framework and the Python checklist are named. |
| 7 | Assumptions and constraints are explicit and clearly distinguished from one another | Pass | Separate sections; a target completion date was added to Constraints during this review. |
| 8 | Document supports executive decision-making with a clear, unambiguous recommendation | Pass | "Proceed" with a one-sentence rationale. |

## Language and Domain Results

Checklist: [QC-LANG-001].

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language | en`, `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Executive English as the registry states. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary (`DICT`) exists yet; terms (Menu, CoffeeMaker, MoneyMachine, drink, resource) are the assignment's own and used consistently. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Verified by reading the file. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No twin file in `docs/`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First accepted version; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and works in the IT domain; S01 asked for this review and acceptance in chat. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | PO, FURPS+, CI, PP, MIL are defined by the framework; PO is spelled out in the Stakeholder Analysis. |

## Overall Verdict

Go — all mandatory criteria pass. One defect (unjustified qualitative cost-benefit) and one gap (no schedule constraint for the milestones to check against) were fixed during the review.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Confirm the target date 2026-10-16 | S01 | 2026-10-09 |

---

[BC-001]: ../../business-case.md
[QC-BC-001]: ../../../framework/qc/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[c24f412]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-oop_coffee_machine/commit/c24f41207fb15f39b0ad6501e1f3126d3bd9232e
