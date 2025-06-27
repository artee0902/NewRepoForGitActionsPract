import pytest
import allure
from playwright.sync_api import expect

@allure.epic("E-Commerce App")
@allure.feature("Login Functionality")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify valid login redirects to dashboard")
@pytest.mark.order(1)
def test_valid_login(login):
    assert "loginpagePractise" in login.url

@allure.epic("E-Commerce App")
@allure.feature("Cart Functionality")
@allure.story("Add Multiple Products")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Add multiple products to cart and verify")
@pytest.mark.order(2)
def test_add_multiple_products(login):
    products = ["iphone X", "Nokia Edge"]

    for product_name in products:
        product_card = login.locator("app-card").filter(has_text=product_name)
        product_card.get_by_role("button", name="Add").click()

    login.get_by_text("Checkout").click()
    expect(login.locator(".media-body")).to_have_count(len(products))

@allure.epic("E-Commerce App")
@allure.feature("Contact Info")
@allure.story("Popup Handling")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Extract email address from popup window")
@pytest.mark.order(3)
def test_extract_email_from_popup(login):
    with login.expect_popup() as popup_info:
        login.locator(".blinkingText").click()
    popup = popup_info.value

    text = popup.locator(".red").text_content()
    email = text.split("at")[1].strip().split(" ")[0]
    print("Extracted Email:", email)
    assert "@" in email
