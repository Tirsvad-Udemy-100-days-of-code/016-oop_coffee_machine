# Phase 1: Project Setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [c24f412] |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-003 (Go) | [c24f412] |

---

## Purpose

Decide whether the project skeleton, tooling and configuration are ready so that application code can be written on top of them.

## Deliverable

Repository skeleton with `pyproject.toml`, Python `.gitignore`, `src/`, `tests/`, `constants.py`, `Doxyfile` and a CI workflow that runs pytest.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[dev]` succeeds in a fresh `.venv` on Python 3.13+ | Met | Not met |
| 2 | `pytest` runs (collects zero or more tests) without configuration errors | Met | Not met |
| 3 | `[project] dependencies` in `pyproject.toml` is empty | Met | Not met |
| 4 | `.env` and `.venv` are ignored by `.gitignore` | Met | Not met |
| 5 | `doxygen Doxyfile` runs without errors | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First phase |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 2 and 3; success criteria 1 and 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-09 — start of the course project, no external deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Configure the project with `requires-python >= 3.13`, a `src/` layout, no runtime dependencies and pytest as an optional `dev` dependency, so that setup is reproducible for S02. | No |  |
| 2 | Review Python .gitignore | Confirm the Python `.gitignore` ignores `.venv/`, `.env`, caches and generated Doxygen output so tokens and build artefacts never reach the repository (risk in BC-001). | No |  |
| 3 | Create src and tests skeleton with constants.py | Create `src/coffee_machine/` with `__init__.py` and `constants.py` (menu data, resources, coin values, command words) and an empty `tests/` package, following the coding conventions. | No |  |
| 4 | Add Doxyfile | Add a Doxyfile configured for Python (`OPTIMIZE_OUTPUT_JAVA`, input `src/`, output `docs/api/`) so Doxygen comments in the source can be built into documentation. | No |  |
| 5 | Configure CI workflow | Add a CI workflow for the git host that creates a venv, installs the project with the `dev` extra and runs pytest on Python 3.13, to be described in the README. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[c24f412]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-oop_coffee_machine/commit/c24f41207fb15f39b0ad6501e1f3126d3bd9232e
