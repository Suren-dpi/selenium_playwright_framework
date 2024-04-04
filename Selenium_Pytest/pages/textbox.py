from selenium.webdriver.common.by import By
from Selenium_Pytest.pages.base_page import BasePage
import time

class Textbox(BasePage):
    URL = "https://demoqa.com/text-box"

    USERNAME_FIELD = (By.XPATH, "//input[@id='userName']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH,"//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH,"//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
    V_NAME = (By.XPATH,"//p[@id='name']")
    V_EMAIL = (By.XPATH, "//p[@id='email']")
    V_CADD = (By.XPATH, "//p[@id='currentAddress']")
    V_PADD = (By.XPATH, "//p[@id='permanentAddress']")


    def check_textbox(self, username, email,cur_address,per_address):
        self.driver.get(self.URL)
        self.entertext(self.USERNAME_FIELD,username)
        self.entertext(self.EMAIL_FIELD,email)
        self.entertext(self.CURRENT_ADDRESS, cur_address)
        self.entertext(self.PERMANENT_ADDRESS, per_address)
        self.scrollto_element(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)
        name = self.gettext(self.V_NAME)
        mail = self.gettext(self.V_EMAIL)
        cadd = self.gettext(self.V_CADD)
        padd = self.gettext(self.V_PADD)
        assert username in name
        assert email in mail
        assert cur_address in cadd
        assert per_address in padd
