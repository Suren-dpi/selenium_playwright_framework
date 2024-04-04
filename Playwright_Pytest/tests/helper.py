import pytest
from datetime import datetime
import os
path = os.getcwd()
parentpath = os.path.abspath(os.path.join(path, os.pardir))

curdatetime = lambda : datetime.now().strftime("%y%m%d%H%M%S")
class Base:

    def __init__(self,page):
        self.page=page

    def screenshot(self):
        self.page.screenshot(path=parentpath + "/tests/screenshots/" + str(curdatetime()) + ".png", full_page=True)

    def navigate(self,url):
        try:
            self.page.goto(url)
        except BaseException as e:
            print(url,str(e))
            self.screenshot()
            pytest.fail(url,str(e))

    def wait_for_selector(self,selector):
        try:
            return self.page.wait_for_selector(selector)
        except BaseException as e:
            print(selector,str(e))
            self.screenshot()
            pytest.fail(selector,str(e))

    def click(self,selector):
        try:
            self.page.click(selector)
        except BaseException as e:
            print(selector,str(e))
            self.screenshot()
            pytest.fail(selector,str(e))

    def type(self,selector,text):
        try:
            self.page.type(selector,text)
        except BaseException as e:
            print(selector,str(e))
            self.screenshot()
            pytest.fail(selector,str(e))

    def get_text(self,selector):
        try:
            return self.page.text_content(selector)
        except BaseException as e:
            print(selector,str(e))
            self.screenshot()
            pytest.fail(selector,str(e))

    def fill(self,selector,text):
        try:
            self.page.fill(selector,text)
        except BaseException as e:
            print(selector,str(e))
            self.screenshot()
            pytest.fail(selector,str(e))

    def send_keys(self,keys):
        try:
            # Press the "Enter" key
            self.page.keyboard.press(keys)
        except BaseException as e:
            print(keys,str(e))
            self.screenshot()
            pytest.fail(keys,str(e))

    def send_inp_files(self, selector,path):
        try:
            # Press the "Enter" key
            self.page.set_input_files(selector,path)
        except BaseException as e:
            print(selector, str(e))
            self.screenshot()
            pytest.fail(selector, str(e))



