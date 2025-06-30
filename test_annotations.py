import allure
from playwright.sync_api import Page, expect


@allure.epic("User Authentication")
@allure.feature("Login Functionality")
@allure.story("Valid login scenario")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Tests login with valid credentials and checks for navigation to the dashboard.")
@allure.link("https://rahulshettyacademy.com/loginpagePractise/", name="Live Site")

def test_login_success(page: Page):
    with allure.step("Open login page"):
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with allure.step("Enter valid username and password"):
        page.fill("#username", "rahulshettyacademy")
        page.fill("#password", "learning")

    with allure.step("Click on sign-in button"):
        page.click("#signInBtn")

    with allure.step("Wait for navigation to shop page"):
        page.wait_for_url("**/angularpractice/shop")
        assert "angularpractice/shop" in page.url, "Did not navigate to shop page after login"

    with allure.step("Verify products are visible on the dashboard"):
        product_cards = page.locator("app-card")
        assert product_cards.count() > 0, "No product cards found after login"
