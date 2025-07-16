import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set False to debug locally
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


#
# #def page():
#     page.goto()
