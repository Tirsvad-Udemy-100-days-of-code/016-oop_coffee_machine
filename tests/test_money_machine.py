"""! @file
@brief Tests for MoneyMachine.
"""

import pytest

from coffee_machine.money_machine import MoneyMachine
from tests.conftest import InputFeeder


def test_report_prints_profit(capsys: pytest.CaptureFixture[str]) -> None:
    MoneyMachine().report()

    assert capsys.readouterr().out == "Money: $0.00\n"


def test_process_coins_adds_up_coin_values(feed_input: InputFeeder) -> None:
    feed_input(["1", "2", "3", "4"])  # quarters, dimes, nickels, pennies

    assert MoneyMachine().process_coins() == pytest.approx(0.64)


def test_process_coins_asks_again_on_invalid_count(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input(["abc", "-1", "4", "0", "0", "0"])

    assert MoneyMachine().process_coins() == pytest.approx(1.0)
    assert capsys.readouterr().out.count("whole number") == 2


def test_make_payment_with_exact_amount_keeps_profit(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input(["6", "0", "0", "0"])  # $1.50
    machine = MoneyMachine()

    assert machine.make_payment(1.5)
    assert machine.profit == pytest.approx(1.5)
    assert "change" not in capsys.readouterr().out


def test_make_payment_with_excess_gives_change(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input(["12", "0", "0", "0"])  # $3.00 for a $2.50 drink
    machine = MoneyMachine()

    assert machine.make_payment(2.5)
    assert machine.profit == pytest.approx(2.5)
    assert "$0.50 in change" in capsys.readouterr().out


def test_make_payment_when_short_refunds_and_keeps_no_profit(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input(["1", "0", "0", "0"])
    machine = MoneyMachine()

    assert not machine.make_payment(1.5)
    assert machine.profit == 0.0
    assert "Money refunded" in capsys.readouterr().out
