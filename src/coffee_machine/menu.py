"""! @file
@brief Menu of drinks the coffee machine can make.
"""

from collections.abc import Mapping
from dataclasses import dataclass

from coffee_machine import constants


@dataclass(frozen=True)
class MenuItem:
    """! @brief A drink with its price and the ingredients it needs."""

    name: str
    cost: float
    ingredients: Mapping[str, int]


class Menu:
    """! @brief The list of drinks that can be ordered."""

    def __init__(self) -> None:
        """! @brief Build the menu from the drinks in constants.py."""
        self._items: list[MenuItem] = [
            MenuItem(name, cost, constants.DRINK_INGREDIENTS[name])
            for name, cost in constants.DRINK_COSTS.items()
        ]

    def get_items(self) -> str:
        """! @brief Return the drink names for the prompt, e.g. "espresso/latte".

        @return The drink names joined by the menu separator.
        """
        return constants.MENU_SEPARATOR.join(item.name for item in self._items)

    def find_drink(self, order_name: str) -> MenuItem | None:
        """! @brief Look up a drink by name.

        Prints a message when the drink does not exist.

        @param order_name The name the user typed.
        @return The matching item, or None when the drink is not on the menu.
        """
        for item in self._items:
            if item.name == order_name:
                return item
        print(constants.MSG_UNAVAILABLE)
        return None
