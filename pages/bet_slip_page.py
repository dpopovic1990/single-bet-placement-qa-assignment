from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BetSlipPage(BasePage):

    STAKE_INPUT = (
        By.ID,
        "bet-slip-stake-input",
    )

    PLACE_BET_BUTTON = (
        By.ID,
        "bet-slip-place-bet",
    )

    def enter_stake(self, stake):
        stake_input = self.wait_for_visible(self.STAKE_INPUT)

        stake_input.clear()
        stake_input.send_keys(str(stake))

    def place_bet(self):
        self.wait_for_clickable(
            self.PLACE_BET_BUTTON
        ).click()