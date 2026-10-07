# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [c24f412] |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Added RC-007 (source code review) to the MIL-002 row | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that traceability is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | [RC-006] |
| [MIL-001] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-003] |
| [MIL-002] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-004], [RC-007] |
| [MIL-003] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-005] |

## Coverage Notes

No KPI, use case, user story or design artifact exists yet: the course supplies the design, so the tasks in the milestones are plain tasks. `-` in Upstream means foundational; in Downstream it means nothing is built on it yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-setup.md
[MIL-002]: ../milestones/mil-002-core.md
[MIL-003]: ../milestones/mil-003-docs.md
[RC-001]: reviews/rc-001-business-case.md
[RC-002]: reviews/rc-002-stakeholder-analysis.md
[RC-003]: reviews/rc-003-mil-001.md
[RC-004]: reviews/rc-004-mil-002.md
[RC-005]: reviews/rc-005-mil-003.md
[RC-006]: reviews/rc-006-project-plan.md
[RC-007]: reviews/rc-007-source-code-mil-002.md
[c24f412]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-oop_coffee_machine/commit/c24f41207fb15f39b0ad6501e1f3126d3bd9232e
