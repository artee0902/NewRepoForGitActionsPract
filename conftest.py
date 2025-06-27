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
        browser = p.chromium.launch(headless=False)  # Change to True for CI
        context = browser.new_context()
        page = context.new_page()
        page.goto(config["url"])

        # Ensure page is loaded
        page.wait_for_load_state("domcontentloaded")
        yield page

        context.close()
        browser.close()

@pytest.fixture(scope="function")
def login(page):
    from pages.login_page import LoginPage

    login_page = LoginPage(page)

    # Perform login with safe checks
    login_page.login(config["username"], config["password"], config["role"])

    # Wait for post-login page (adjust selector or URL as needed)
    try:
        page.wait_for_url("**/shop", timeout=10000)
  # Adjust this if dashboard URL differs
    except:
        pytest.fail("Login failed or dashboard did not load in time.")

    return page
