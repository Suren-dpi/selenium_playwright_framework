from selenium.webdriver.common.by import By
from Selenium_Pytest.pages.base_page import BasePage
import time
class Form(BasePage):
    URL = "https://demoqa.com/automation-practice-form"


    FIRSTNAME = (By.XPATH,"//input[@id='firstName']")
    LASTNAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    GENDER_MALE = (By.XPATH, "//*[@value='Male']/../label")
    GENDER_FEMALE = (By.XPATH, "//*[@value='Female']/../label")
    GENDER_OTHER = (By.XPATH, "//*[@value='Other']/../label")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DOB = (By.XPATH, "//input[@id='dateOfBirthInput']")
    SUBJECTS = (By.XPATH, "//input[@id='subjectsInput']")
    HOBBIES = (By.XPATH, "//input[@id='hobbies - checkbox - 1']")
    UPLOAD = (By.XPATH,"//input[@id='uploadPicture']")
    CUR_ADD = (By.XPATH, "//textarea[@id='currentAddress']")

    def practice_form(self,firstname,lastanme,email,gender,mobile,dob,subjects,hobbies):
        self.driver.get(self.URL)
        self.entertext(self.FIRSTNAME,firstname)
        self.entertext(self.LASTNAME,lastanme)
        self.entertext(self.EMAIL,email)
        if gender == 'Male':
            self.scrollto_element(self.GENDER_MALE)
            self.click(self.GENDER_MALE)
        if gender == 'Female':
            self.click(self.GENDER_FEMALE)
        else:
            self.click(self.GENDER_OTHER)
        self.entertext(self.MOBILE,mobile)
        self.replacetext(self.DOB,dob)
        time.sleep(2)
        self.entertext(self.SUBJECTS,subjects)
        self.entertext(self.HOBBIES,hobbies)

