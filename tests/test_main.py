"""! @file
@brief Tests for the main loop.
"""

import pytest

from coffee_machine.main import main
from tests.conftest import InputFeeder

PAY_150 = ["6", "0", "0", "0"]
PAY_250 = ["10", "0", "0", "0"]
PAY_NOTHING = ["0", "0", "0", "0"]


def test_off_stops_the_loop(feed_input: InputFeeder) -> None:
    feed_input(["off"])

    main()


def test_report_shows_resources_and_money(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input(["report", "off"])

    main()

    out = capsys.readouterr().out
    assert "Water: 300ml" in out
    assert "Money: $0.00" in out


def test_successful_order_makes_drink_and_updates_report(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input(["espresso", *PAY_150, "report", "off"])

    main()

    out = capsys.readouterr().out
    assert "Here is your espresso" in out
    assert "Water: 250ml" in out
    assert "Money: $1.50" in out


def test_choice_is_case_insensitive(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input([" Espresso ", *PAY_150, "off"])

    main()

    assert "Here is your espresso" in capsys.readouterr().out


def test_unknown_drink_asks_again_without_payment(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input(["tea", "off"])

    main()

    out = capsys.readouterr().out
    assert "not available" in out
    assert "insert coins" not in out


def test_insufficient_resources_stop_before_payment(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    # The second latte needs 150 ml milk but only 50 ml is left.
    feed_input(["latte", *PAY_250, "latte", "off"])

    main()

    out = capsys.readouterr().out
    assert out.count("insert coins") == 1
    assert "not enough milk" in out


def test_short_payment_is_refunded_and_no_drink_is_made(
    feed_input: InputFeeder, capsys: pytest.CaptureFixture[str]
) -> None:
    feed_input(["espresso", *PAY_NOTHING, "report", "off"])

    main()

    out = capsys.readouterr().out
    assert "Money refunded" in out
    assert "Enjoy" not in out
    assert "Water: 300ml" in out
