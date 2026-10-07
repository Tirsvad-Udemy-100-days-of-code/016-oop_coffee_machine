"""! @file
@brief Constants for the coffee machine: menu, resources, coins and commands.
"""

from typing import Final

## @name Ingredient names
## @{
WATER: Final = "water"
MILK: Final = "milk"
COFFEE: Final = "coffee"
## @}

## @brief Cost in dollars and ingredient amounts per drink.
MENU: Final[dict[str, dict[str, object]]] = {
    "espresso": {"cost": 1.5, "ingredients": {WATER: 50, MILK: 0, COFFEE: 18}},
    "latte": {"cost": 2.5, "ingredients": {WATER: 200, MILK: 150, COFFEE: 24}},
    "cappuccino": {"cost": 3.0, "ingredients": {WATER: 250, MILK: 100, COFFEE: 24}},
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

## @name Commands at the prompt
## @{
COMMAND_OFF: Final = "off"
COMMAND_REPORT: Final = "report"
## @}
