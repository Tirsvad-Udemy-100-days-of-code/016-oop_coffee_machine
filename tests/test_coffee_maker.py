"""! @file
@brief Tests for CoffeeMaker.
"""

import pytest

from coffee_machine import constants
from coffee_machine.coffee_maker import CoffeeMaker
from coffee_machine.menu import Menu, MenuItem


def _drink(name: str) -> MenuItem:
    drink = Menu().find_drink(name)
    assert drink is not None
    return drink


def test_report_prints_each_resource_with_unit(
    capsys: pytest.CaptureFixture[str],
) -> None:
    CoffeeMaker().report()

    assert capsys.readouterr().out.splitlines() == [
        "Water: 300ml",
        "Milk: 200ml",
        "Coffee: 100g",
    ]


def test_is_resource_sufficient_when_enough() -> None:
    assert CoffeeMaker().is_resource_sufficient(_drink("latte"))


def test_is_resource_sufficient_when_exactly_enough() -> None:
    maker = CoffeeMaker()
    maker.resources.update(
        {constants.WATER: 50, constants.MILK: 0, constants.COFFEE: 18}
    )

    assert maker.is_resource_sufficient(_drink("espresso"))


def test_is_resource_sufficient_when_short_names_each_missing_ingredient(
    capsys: pytest.CaptureFixture[str],
) -> None:
    maker = CoffeeMaker()
    maker.resources.update({constants.WATER: 10, constants.MILK: 10})

    assert not maker.is_resource_sufficient(_drink("latte"))
    out = capsys.readouterr().out
    assert "not enough water" in out
    assert "not enough milk" in out
    assert "not enough coffee" not in out


def test_make_coffee_deducts_ingredients_and_serves(
    capsys: pytest.CaptureFixture[str],
) -> None:
    maker = CoffeeMaker()

    maker.make_coffee(_drink("latte"))

    assert maker.resources == {
        constants.WATER: 100,
        constants.MILK: 50,
        constants.COFFEE: 76,
    }
    assert "latte" in capsys.readouterr().out
