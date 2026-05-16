from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    MATCH_CARD = (
        By.ID,
        "match-card-premier-league-manutd-chelsea",
    )

    HOME_ODDS_BUTTON = (
        By.ID,
        "odds-premier-league-manutd-chelsea-home",
    )

    def is_match_visible(self):
        return self.wait_for_visible(self.MATCH_CARD).is_displayed()

    def select_home_odds(self):
        self.wait_for_clickable(self.HOME_ODDS_BUTTON).click()