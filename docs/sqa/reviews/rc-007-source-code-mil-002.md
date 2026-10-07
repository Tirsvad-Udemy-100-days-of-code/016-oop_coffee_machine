# Review: Source code of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Review record | [2b6b3be] |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted by S01 (Go) | [26d87d0] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002] (the source code under `src/coffee_machine/` and `tests/` that delivers it)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type, source code)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing | Pass | `coffee_machine`, `CoffeeMaker`, `is_resource_sufficient`, `WATER`; checked by ruff rule set `N`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations | Pass | Assignment names kept (`get_items`, `find_drink`, `make_payment`, `make_coffee`); no abbreviations. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` and `ruff check` clean; no `noqa` or `type: ignore` in the code. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` passes on `src` and `tests`. |
| 5 | No bare `except:`, no swallowed exceptions | Pass | No `try`/`except` in the code. Invalid coin counts are handled by validation, not exceptions. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | None found; `conftest.py` uses `_prompt=""`, an immutable default. |
| 7 | Files, locks and connections are managed with context managers | N-A | The program opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | All public items have Doxygen docstrings; Doxygen builds without warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `print` is the program's user interface (the assignment's required prompts and messages), not logging. No secrets or personal data. The code never reads `.env`. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No DCD exists: the course supplies the design (see PP-001 Open Issues). The classes follow the assignment's `Menu`, `MenuItem`, `CoffeeMaker`, `MoneyMachine`. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 25 tests cover each class and the main loop; `input` is replaced with a fixture; no order or network dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` clean; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies. Dev tools have lower bounds only, which suits a learning project. |

## Overall Verdict

Go — all mandatory criteria pass or are not applicable with a stated reason. Verified by running `ruff format`, `ruff check`, `mypy --strict`, `pytest` (25 passed) and `doxygen Doxyfile` (no warnings), and by a manual run of the program.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether a DCD or use case is wanted for the program (criterion 10) | S01 | 2026-10-14 |

---

[MIL-002]: ../../milestones/mil-002-core.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[2b6b3be]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-oop_coffee_machine/commit/2b6b3bee46e99d487792c79f722a79f9c921304d
[26d87d0]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/016-oop_coffee_machine/commit/26d87d0d0ee63eaefa32e6a71142cfa5397361c7
