import time
from Playwright_Pytest.tests.helper import Base

class Form(Base):
    URL = "https://demoqa.com/automation-practice-form"

    FIRSTNAME = ("//input[@id='firstName']")
    LASTNAME = ("//input[@id='lastName']")
    EMAIL = ("//input[@id='userEmail']")
    GENDER_MALE = ("//*[@value='Male']/../label")
    GENDER_FEMALE = ("//*[@value='Female']/../label")
    GENDER_OTHER = ("//*[@value='Other']/../label")
    MOBILE = ("//input[@id='userNumber']")
    DOB = ("//input[@id='dateOfBirthInput']")
    SUBJECTS = ("//input[@id='subjectsInput']")
    HOBBIES_SPORTS = ("//*[@id='hobbiesWrapper']//label[contains(text(),'Sports')]")
    HOBBIES_READING = ("//*[@id='hobbiesWrapper']//label[contains(text(),'Reading')]")
    HOBBIES_MUSIC = ("//*[@id='hobbiesWrapper']//label[contains(text(),'Music')]")
    UPLOAD = ("//input[@id='uploadPicture']")
    CUR_ADD = ("//textarea[@id='currentAddress']")
    STATE = ("//*[@id='state']")
    CITY = ("//*[@id='city']")
    SUBMIT = ("//*[@id='submit']")


    def formfill(self,firstname,lastanme,email,gender,mobile,dob,subjects,hobbies):
        self.navigate(self.URL)
        self.type(self.FIRSTNAME, firstname)
        self.type(self.LASTNAME, lastanme)
        self.type(self.EMAIL, email)
        if gender == 'Male':
            self.click(self.GENDER_MALE)
        if gender == 'Female':
            self.click(self.GENDER_FEMALE)
        else:
            self.click(self.GENDER_OTHER)
        self.type(self.MOBILE, mobile)
        self.fill(self.DOB, dob)
        self.send_keys('Enter')
        if hobbies == 'Sports':
            self.click(self.HOBBIES_SPORTS)
        elif hobbies == 'Reading':
            self.click(self.HOBBIES_READING)
        else:
            self.click(self.HOBBIES_MUSIC)
        self.type(self.SUBJECTS, subjects)
        self.send_inp_files(self.UPLOAD,"C:\\Users\\surendharan.jayaprak\\Desktop\\BrandEMI_ECS.png")
        self.type(self.CUR_ADD,"5/1319A VP singh street, lakkiyampatti Dharmapuri")
        self.click(self.STATE)
        self.type(self.STATE,"Haryana")
        self.send_keys('Enter')
        self.click(self.CITY)
        self.type(self.CITY, "Karnal")
        self.send_keys('Tab')
        self.click(self.SUBMIT)
        time.sleep(10)
