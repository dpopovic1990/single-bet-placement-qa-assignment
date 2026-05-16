import pytest

from pages.home_page import HomePage
from pages.bet_slip_page import BetSlipPage
from pages.receipt_modal import ReceiptModal


@pytest.mark.ui
def test_user_can_successfully_place_single_bet(driver):
    """
    Chosen as the UI automation test because it validates
    the application's primary revenue-generating user journey,
    including match selection, stake entry, bet placement,
    and successful receipt confirmation.
    """

    home_page = HomePage(driver)
    bet_slip_page = BetSlipPage(driver)
    receipt_modal = ReceiptModal(driver)

    assert home_page.is_match_visible()

    home_page.select_home_odds()

    bet_slip_page.enter_stake(5)

    bet_slip_page.place_bet()

    assert receipt_modal.is_success_modal_displayed()