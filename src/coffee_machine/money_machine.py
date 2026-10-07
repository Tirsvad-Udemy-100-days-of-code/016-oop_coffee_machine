"""! @file
@brief The part of the machine that takes coins and keeps the profit.
"""

from coffee_machine import constants


class MoneyMachine:
    """! @brief Processes coins, gives change and keeps the profit."""

    def __init__(self) -> None:
        """! @brief Start with the initial profit and no money received."""
        self.profit: float = constants.INITIAL_PROFIT
        self.money_received: float = 0.0

    def report(self) -> None:
        """! @brief Print the money in the machine."""
        print(f"Money: {constants.CURRENCY}{self.profit:.{constants.MONEY_DECIMALS}f}")

    def process_coins(self) -> float:
        """! @brief Ask for each coin type and add up the value.

        @return The total value of the coins inserted, in dollars.
        """
        print(constants.MSG_INSERT_COINS)
        total = 0.0
        for coin, value in constants.COIN_VALUES.items():
            total += self._ask_count(coin) * value
        self.money_received = round(total, constants.MONEY_DECIMALS)
        return self.money_received

    def make_payment(self, cost: float) -> bool:
        """! @brief Take coins for a drink, give change or refund.

        @param cost The price of the drink in dollars.
        @return True when enough money was inserted.
        """
        self.process_coins()
        if self.money_received < cost:
            print(constants.MSG_NOT_ENOUGH_MONEY)
            self.money_received = 0.0
            return False
        change = round(self.money_received - cost, constants.MONEY_DECIMALS)
        if change > 0:
            print(
                constants.MSG_CHANGE.format(currency=constants.CURRENCY, change=change)
            )
        self.profit += cost
        self.money_received = 0.0
        return True

    @staticmethod
    def _ask_count(coin: str) -> int:
        """! @brief Ask how many coins of one type until a valid count is given."""
        while True:
            answer = input(constants.MSG_COIN_PROMPT.format(coin=coin))
            if answer.strip().isdigit():
                return int(answer)
            print(constants.MSG_INVALID_COUNT)
