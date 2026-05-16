import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config import FULL_URL


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(FULL_URL)

    yield driver

    driver.quit()