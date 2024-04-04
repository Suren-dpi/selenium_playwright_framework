from Playwright_Pytest.pages.textbox import TextBox
from Playwright_Pytest.pages.formfill import Form
import pytest

@pytest.mark.usefixtures('page')
class Test_demoqa:

    def test_texbox_page(self,page):
        tt = TextBox(page)
        tt.textbox('Suren', 'Suren@gamil.com', 'Bangalore', 'Dharmapuri')

    def test_formfill(self,page):
        ff = Form(page)
        ff.formfill('Suren','Prakash','Suren@gmail.com','Male','9876543210','25-01-1990','maths,science','Reading')


