"""! @file
@brief The part of the machine that holds ingredients and makes drinks.
"""

from coffee_machine import constants
from coffee_machine.menu import MenuItem


class CoffeeMaker:
    """! @brief Holds the resources and makes the drinks."""

    def __init__(self) -> None:
        """! @brief Fill the machine with the initial resources."""
        self.resources: dict[str, int] = dict(constants.INITIAL_RESOURCES)

    def report(self) -> None:
        """! @brief Print the amount left of each resource."""
        for ingredient, amount in self.resources.items():
            unit = constants.RESOURCE_UNITS[ingredient]
            print(f"{ingredient.capitalize()}: {amount}{unit}")

    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        """! @brief Check that every ingredient of the drink is available.

        Prints a message for each ingredient that is short.

        @param drink The drink the user ordered.
        @return True when the machine can make the drink.
        """
        is_sufficient = True
        for ingredient, required in drink.ingredients.items():
            if required > self.resources[ingredient]:
                print(constants.MSG_INSUFFICIENT_RESOURCE.format(ingredient=ingredient))
                is_sufficient = False
        return is_sufficient

    def make_coffee(self, order: MenuItem) -> None:
        """! @brief Deduct the ingredients and serve the drink.

        @param order The drink to make; resources must already be sufficient.
        """
        for ingredient, required in order.ingredients.items():
            self.resources[ingredient] -= required
        print(constants.MSG_ENJOY.format(drink=order.name))
