"""! @file
@brief Checks that the constants are consistent with each other.
"""

from coffee_machine import constants


def test_every_drink_has_a_cost_and_ingredients() -> None:
    assert set(constants.DRINK_COSTS) == set(constants.DRINK_INGREDIENTS)


def test_every_drink_uses_known_ingredients() -> None:
    known = set(constants.INITIAL_RESOURCES)
    for ingredients in constants.DRINK_INGREDIENTS.values():
        assert set(ingredients) <= known


def test_every_resource_has_a_unit() -> None:
    assert set(constants.INITIAL_RESOURCES) == set(constants.RESOURCE_UNITS)


def test_commands_are_not_drink_names() -> None:
    assert constants.COMMAND_OFF not in constants.DRINK_COSTS
    assert constants.COMMAND_REPORT not in constants.DRINK_COSTS
