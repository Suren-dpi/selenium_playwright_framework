from Playwright_Pytest.tests.helper import Base

class TextBox(Base):
    URL = "https://demoqa.com/text-box"

    USERNAME_FIELD = ("//input[@id='userName']")
    EMAIL_FIELD = ("//input[@id='userEmail']")
    CURRENT_ADDRESS = ("//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = ("//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = ("//button[@id='submit']")
    V_NAME = ("//p[@id='name']")
    V_EMAIL = ("//p[@id='email']")
    V_CADD = ("//p[@id='currentAddress']")
    V_PADD = ("//p[@id='permanentAddress']")

    def textbox(self,username,email,cur_address,per_address):
        self.navigate(self.URL)
        self.type(self.USERNAME_FIELD, username)
        self.type(self.EMAIL_FIELD, email)
        self.type(self.CURRENT_ADDRESS, cur_address)
        self.type(self.PERMANENT_ADDRESS, per_address)
        self.click(self.SUBMIT_BUTTON)
        name = self.get_text(self.V_NAME)
        mail = self.get_text(self.V_EMAIL)
        cadd = self.get_text(self.V_CADD)
        padd = self.get_text(self.V_PADD)
        assert username in name
        assert email in mail
        assert cur_address in cadd
        assert per_address in padd
