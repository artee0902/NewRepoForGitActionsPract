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
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(config["url"])
        yield page
        browser.close()

@pytest.fixture(scope="function")
def login(page):
    from pages.login_page import LoginPage
    login_page = LoginPage(page)
    login_page.login(config["username"], config["password"], config["role"])
    return page

