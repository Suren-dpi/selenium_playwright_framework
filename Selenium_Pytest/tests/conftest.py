import pytest
from Selenium_Pytest.utils.driver_manager import DriverManager

@pytest.fixture(scope='session')
def driver():
    driver = DriverManager.get_chromedriver()
    yield driver
    driver.quit()