from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ReceiptModal(BasePage):

    SUCCESS_MODAL = (
        By.ID,
        "modal-success",
    )

    CLOSE_BUTTON = (
        By.ID,
        "modal-success-close",
    )

    def is_success_modal_displayed(self):
        return self.wait_for_visible(
            self.SUCCESS_MODAL
        ).is_displayed()

    def close_modal(self):
        self.wait_for_clickable(
            self.CLOSE_BUTTON
        ).click()