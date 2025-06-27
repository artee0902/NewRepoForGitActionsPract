import pytest
import json
import os
from playwright.sync_api import sync_playwright

# Load config once
config_path = os.path.join(os.path.dirname(__file__), 'tests', 'config.json')
with open(config_path) as f:
    config = json.load(f)

@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless=True for CI
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def login(page):
    # Navigate explicitly to login page URL every time before login
    page.goto(config["url"])

    from pages.login_page import LoginPage
    login_page = LoginPage(page)

    login_page.login(config["username"], config["password"], config["role"])

    # Wait for URL after login to confirm success (adjust if needed)
    page.wait_for_url("**/shop", timeout=10000)
    return page
