from selenium.webdriver.common.by import By
from Selenium_Pytest.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"

    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, "submit")

    def qa_login(self, username, password):
        self.driver.get(self.URL)
        self.entertext(self.USERNAME_FIELD,username)
        self.entertext(self.PASSWORD_FIELD,password)
        self.click(self.LOGIN_BUTTON)
