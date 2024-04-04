import pytest
from Selenium_Pytest.pages.base_page import BasePage
from Selenium_Pytest.pages.login_page import LoginPage
from Selenium_Pytest.pages.textbox import Textbox
from Selenium_Pytest.pages.form import Form
import time

@pytest.mark.usefixtures('driver')
class TestLogin:
    # def test_successful_login(self, driver):
    #     login_page = LoginPage(driver)
    #     bp = BasePage(driver)
    #     login_page.qa_login('student', 'Password123')
    #     time.sleep(2)
    #     bp.screenshot('test.png')
    #     driver.quit()

    def test_textbox(self,driver):
        textbox = Textbox(driver)
        textbox.check_textbox('Suren','Suren@gamil.com','Bangalore','Dharmapuri')

    def test_form(self,driver):
        form = Form(driver)
        form.practice_form('Suren','Prakash','Suren@gmail.com','Others','9876543210','25-01-1990','maths,science','Reading,playing')





