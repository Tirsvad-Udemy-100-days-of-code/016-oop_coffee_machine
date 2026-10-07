"""! @file
@brief Tests for Menu and MenuItem.
"""

import pytest

from coffee_machine import constants
from coffee_machine.menu import Menu


def test_get_items_lists_all_drinks_separated() -> None:
    assert Menu().get_items() == "espresso/latte/cappuccino"


def test_find_drink_returns_matching_item() -> None:
    drink = Menu().find_drink("latte")

    assert drink is not None
    assert drink.name == "latte"
    assert drink.cost == constants.DRINK_COSTS["latte"]
    assert drink.ingredients == constants.DRINK_INGREDIENTS["latte"]


def test_find_drink_when_unknown_returns_none_and_prints_message(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert Menu().find_drink("tea") is None
    assert constants.MSG_UNAVAILABLE in capsys.readouterr().out
