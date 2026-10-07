"""! @file
@brief Shared test helpers.
"""

from collections.abc import Callable, Iterable

import pytest

InputFeeder = Callable[[Iterable[str]], None]


@pytest.fixture
def feed_input(monkeypatch: pytest.MonkeyPatch) -> InputFeeder:
    """! @brief Return a function that makes input() answer from a list."""

    def feed(answers: Iterable[str]) -> None:
        iterator = iter(answers)
        monkeypatch.setattr("builtins.input", lambda _prompt="": next(iterator))

    return feed
