"""! @file
@brief Checks that the constants are consistent with each other.
"""

from coffee_machine import constants


def test_every_drink_uses_known_ingredients() -> None:
    known = set(constants.INITIAL_RESOURCES)
    for drink in constants.MENU.values():
        assert set(drink["ingredients"]) <= known  # type: ignore[call-overload]


def test_every_resource_has_a_unit() -> None:
    assert set(constants.INITIAL_RESOURCES) == set(constants.RESOURCE_UNITS)


def test_commands_are_not_drink_names() -> None:
    assert constants.COMMAND_OFF not in constants.MENU
    assert constants.COMMAND_REPORT not in constants.MENU
