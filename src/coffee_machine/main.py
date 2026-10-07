"""! @file
@brief Entry point: keeps the coffee machine running until it is turned off.
"""

from coffee_machine import constants
from coffee_machine.coffee_maker import CoffeeMaker
from coffee_machine.menu import Menu
from coffee_machine.money_machine import MoneyMachine


def main() -> None:
    """! @brief Run the machine until the user types the off command.

    Asks for a drink, checks the resources, takes payment and then makes it.
    """
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        choice = input(constants.PROMPT_TEMPLATE.format(items=menu.get_items()))
        choice = choice.strip().lower()
        if choice == constants.COMMAND_OFF:
            break
        if choice == constants.COMMAND_REPORT:
            coffee_maker.report()
            money_machine.report()
            continue
        drink = menu.find_drink(choice)
        if (
            drink is not None
            and coffee_maker.is_resource_sufficient(drink)
            and money_machine.make_payment(drink.cost)
        ):
            coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
