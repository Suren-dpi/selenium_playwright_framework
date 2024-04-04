import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

path = os.getcwd()
parentpath = os.path.abspath(os.path.join(path, os.pardir))

class DriverManager:
    def download_chromedriver(self):
        driverurl=''
        url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
        response = requests.request('GET', url)
        res = response.json()
        print(res)
        links = res['channels']['Stable']['downloads']['chromedriver']
        for x in links:
            if x['platform'] == 'win64':
                driverurl = x['url']
        return driverurl

    @staticmethod
    def get_chromedriver():
        service = Service(parentpath + r"/browserdrivers/chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        # options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    @staticmethod
    def get_firefoxdriver():
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        return driver

    @staticmethod
    def get_edgedriver():
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        driver.maximize_window()
        return driver
