"""! @file
@brief Constants for the coffee machine: menu, resources, coins, commands, messages.
"""

from typing import Final

## @name Ingredient names
## @{
WATER: Final = "water"
MILK: Final = "milk"
COFFEE: Final = "coffee"
## @}

## @brief Price in dollars of each drink.
DRINK_COSTS: Final[dict[str, float]] = {
    "espresso": 1.5,
    "latte": 2.5,
    "cappuccino": 3.0,
}

## @brief Amount of each ingredient needed for one drink.
DRINK_INGREDIENTS: Final[dict[str, dict[str, int]]] = {
    "espresso": {WATER: 50, MILK: 0, COFFEE: 18},
    "latte": {WATER: 200, MILK: 150, COFFEE: 24},
    "cappuccino": {WATER: 250, MILK: 100, COFFEE: 24},
}

## @brief Amount of each ingredient the machine starts with.
INITIAL_RESOURCES: Final[dict[str, int]] = {WATER: 300, MILK: 200, COFFEE: 100}

## @brief Units used when reporting each resource.
RESOURCE_UNITS: Final[dict[str, str]] = {WATER: "ml", MILK: "ml", COFFEE: "g"}

## @brief Value in dollars of each accepted coin.
COIN_VALUES: Final[dict[str, float]] = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

## @brief Money in the machine at the start.
INITIAL_PROFIT: Final = 0.0

## @brief Currency symbol shown in messages.
CURRENCY: Final = "$"

## @brief Number of decimals of an amount of money.
MONEY_DECIMALS: Final = 2

## @name Commands at the prompt
## @{
COMMAND_OFF: Final = "off"
COMMAND_REPORT: Final = "report"
## @}

## @name Messages
## @{
PROMPT_TEMPLATE: Final = "What would you like? ({items}): "
MENU_SEPARATOR: Final = "/"
MSG_UNAVAILABLE: Final = "Sorry that item is not available."
MSG_INSUFFICIENT_RESOURCE: Final = "Sorry there is not enough {ingredient}."
MSG_INSERT_COINS: Final = "Please insert coins."
MSG_COIN_PROMPT: Final = "How many {coin}?: "
MSG_INVALID_COUNT: Final = "Please enter a whole number of 0 or more."
MSG_NOT_ENOUGH_MONEY: Final = "Sorry that's not enough money. Money refunded."
MSG_CHANGE: Final = "Here is {currency}{change:.2f} in change."
MSG_ENJOY: Final = "Here is your {drink}. Enjoy!"
## @}
