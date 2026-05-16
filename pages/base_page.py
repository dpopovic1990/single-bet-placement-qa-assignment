from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_all_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_for_text(self, locator, text):
        return self.wait.until(
            EC.text_to_be_present_in_element(locator, text)
        )