# Stakeholder Analysis: OOP Coffee Machine

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-002 (Go) | pending |

---

## Purpose

Identifies who is affected by the coffee machine repository and how closely
each party is managed. Method: Mendelow's power/interest grid, with concerns
mapped to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the assignment with clean code, tests and documentation |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Repository browsers | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews everything.
- **Keep Informed (S02):** cannot change the project but depends on its usability; the README is the channel.
- **Monitor (S03):** casual visitors with no influence; the repository presentation is enough.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Complete, tested assignment solution | Functionality, Reliability |
| S01 | Traceable steps via pull requests | Supportability |
| S02 | Assignment function names kept | Functionality |
| S02 | Run instructions that work | Usability |
| S03 | Clear description, topics and README | Usability |
| S03 | No runtime dependencies | Implementation constraint, Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per phase | Working-tree changes and PRs | MIL-001, MIL-002, MIL-003 |
| S02 | README | Once, updated on change | Setup, run and test instructions | MIL-003 |
| S03 | Repository description, topics, README | Once | Repository presentation | MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants assignment names, while clean Python style prefers other names | S01, S02 | Keep the assignment's method names; follow the style rules elsewhere |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Complete, tested solution | [BC-001] objectives 1 and 2 |
| S02 | Runnable instructions | [BC-001] objective 3 |
| S03 | Presentable repository | [BC-001] objective 4 |

## Sign-Off

| Stakeholder ID | Decision | Date |
| --- | --- | --- |
| S01 | Pending review | |

---

[BC-001]: ./business-case.md
