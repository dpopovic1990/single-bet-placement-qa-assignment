import pytest


@pytest.mark.ui
def test_application_loads(driver):
    assert "Sports Betting QA" in driver.title