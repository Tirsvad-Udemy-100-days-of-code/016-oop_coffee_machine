# Phase 3: Documentation and Publication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [c24f412] |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-005 (Go) | [c24f412] |

---

## Purpose

Decide whether the repository is documented and presentable for S02 and S03.

## Deliverable

README following the course template, generated Doxygen documentation steps, and a repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README has all template sections and the Windows, Debian and macOS venv steps including `python -m pip install --upgrade pip` | Met | Not met |
| 2 | Following the README on a clean clone runs the program and the tests | Met | Not met |
| 3 | `doxygen Doxyfile` produces documentation from the source comments | Met | Not met |
| 4 | Repository description and at least 3 topics are set on the git host | Met | Not met |
| 5 | README and LICENSE agree on the licence | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Documents the finished program |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3 and 4; success criteria 3 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-16 — after Phase 2.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write README | Write `README.md` from the course template: requirements, set-up for Windows PowerShell, Debian and macOS using a local `.venv` and `python -m pip install --upgrade pip`, run, test, CI, Doxygen build, project layout and licence. | No |  |
| 2 | Verify Doxygen build | Run Doxygen on a clean clone and check that classes and methods from the Doxygen comments appear in the output. | No |  |
| 3 | Set repository description and topics | Set a short description and topics on the git host repository (`Tirsvad-Udemy-100_days_of_code`) through its API using the token from `.env`, which stays personal and is never read by the project code. Needs the Product Owner's go-ahead because it changes the remote. | No |  |
| 4 | Verify setup from a clean clone | Follow the README from a fresh clone on the Product Owner's machine and fix any step that does not work. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[c24f412]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-oop_coffee_machine/commit/c24f41207fb15f39b0ad6501e1f3126d3bd9232e
