from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import pytest
from datetime import datetime
path = os.getcwd()
parentpath = os.path.abspath(os.path.join(path, os.pardir))

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.ele_delay=.5
        self.webdriver_delay = 30
        self.wait = WebDriverWait(self.driver, self.webdriver_delay)

    def wait_for_element_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self,locator):
        try:
            time.sleep(self.ele_delay)
            wait = WebDriverWait(self.driver, self.webdriver_delay)
            (wait.until(EC.element_to_be_clickable((locator)))).click()
        except BaseException as e:
            print(str(e))
            self.screenshot(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+'.png')
            pytest.fail(str(e))

    def entertext(self,locator, text):
        time.sleep(self.ele_delay)
        try:
            wait = WebDriverWait(self.driver, self.webdriver_delay)
            (wait.until(EC.element_to_be_clickable((locator)))).send_keys(text)
        except BaseException as e:
            print(str(e))
            self.screenshot(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+'.png')
            pytest.fail(str(e))

    def replacetext(self,locator, text):
        time.sleep(self.ele_delay)
        try:
            wait = WebDriverWait(self.driver, self.webdriver_delay)
            (wait.until(EC.element_to_be_clickable((locator)))).send_keys(Keys.CONTROL,'a',text)
        except BaseException as e:
            print(str(e))
            self.screenshot(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+'.png')
            pytest.fail(str(e))


    def gettext(self,locator):
        try:
            wait = WebDriverWait(self.driver, self.webdriver_delay)
            text = (wait.until(EC.element_to_be_clickable((locator)))).text
            return text
        except BaseException as e:
            print(str(e))
            self.screenshot(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+'.png')
            pytest.fail(str(e))

    def screenshot(self, filename):
        os.chdir(parentpath + "/tests/screenshots")
        self.driver.save_screenshot(filename)
        os.chdir(parentpath+"/tests")

    def scrollto_element(self,locator):
        try:
            js_code = "arguments[0].scrollIntoView();"
            element = self.wait_for_element_visibility(locator)
            self.driver.execute_script(js_code, element)
        except BaseException as e:
            print(str(e))
            self.screenshot(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+'.png')
            pytest.fail(str(e))

