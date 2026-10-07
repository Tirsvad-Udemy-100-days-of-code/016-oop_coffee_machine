# Phase 2: Coffee Machine Program

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after RC-004 (Go) | pending |

---

## Purpose

Decide whether the coffee machine program works as the assignment describes and is covered by tests.

## Deliverable

Python modules `menu`, `coffee_maker`, `money_machine` and `main` under `src/coffee_machine/`, with Doxygen comments, plus pytest tests under `tests/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `Menu.get_items` and `Menu.find_drink` exist and return the menu text and the matching drink or nothing | Met | Not met |
| 2 | `CoffeeMaker.report`, `is_resource_sufficient` and `make_coffee` exist and behave as in the assignment | Met | Not met |
| 3 | `MoneyMachine.report` and `make_payment` exist and behave as in the assignment | Met | Not met |
| 4 | The main loop supports drink choice, `report` and `off` and checks resources before payment | Met | Not met |
| 5 | `pytest` passes and constants come from `constants.py` only | Met | Not met |
| 6 | Code review against `qc-programming-python` has a Go review record | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the skeleton, configuration and CI |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 2; success criteria 1 and 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — after Phase 1.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement Menu and MenuItem | Create `MenuItem` (name, cost, ingredients) and `Menu` with `get_items` (drink names for the prompt) and `find_drink` (returns the item or None for an unknown name), reading data from `constants.py`. | No |  |
| 2 | Implement CoffeeMaker | Create `CoffeeMaker` holding the resources, with `report`, `is_resource_sufficient` (prints which ingredient is short) and `make_coffee` (deducts ingredients). | No |  |
| 3 | Implement MoneyMachine | Create `MoneyMachine` with `report` (profit), and `make_payment` that processes coins, gives change, adds profit and refunds when money is insufficient. | No |  |
| 4 | Implement main loop | Create the entry point that keeps the machine running, accepts a drink name, `report` and `off`, and checks resources before taking payment before making coffee. The course supplies the design, so no separate use case is modelled (see PP-001 Open Issues). | No |  |
| 5 | Write pytest tests | Test each class and the main loop (with patched `input`) for sufficient and insufficient resources, exact, excess and short payment, unknown drink, report and off. | No |  |
| 6 | Review code against qc-programming-python | Review `src/` and `tests/` against the Python checklist and record the result as an RC before the pull request. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
