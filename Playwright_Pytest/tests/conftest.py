import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    # Initialize Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    # Open a new page in the browser
    page = browser.new_page()
    yield page
    # # Optionally, you can close the page after each test
    # page.close()