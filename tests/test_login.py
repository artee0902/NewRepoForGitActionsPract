import pytest
import allure
from playwright.sync_api import expect


@allure.epic("E-Commerce App")
@allure.feature("Login Functionality")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify valid login redirects to dashboard")

def test_valid_login(login):
    # Validate user lands on shop/dashboard page after login
    assert "shop" in login.url.lower() or "dashboard" in login.url.lower()



@allure.epic("E-Commerce App")
@allure.feature("Cart Functionality")
@allure.story("Add Multiple Products")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Add multiple products to cart and verify")

def test_add_multiple_products(login):  # login is the page
    products = ["iphone X", "Nokia Edge"]

    for product_name in products:
        # Use more reliable :has-text locator
        product_card = login.locator(f"app-card:has-text('{product_name}')")
        product_card.locator("button:has-text('Add')").click()

    # Wait for cart button and click it
    checkout_button = login.get_by_text("Checkout")
    checkout_button.wait_for(state="visible", timeout=5000)
    checkout_button.click()

    # Assert number of items in cart
    cart_items = login.locator(".media-body")
    expect(cart_items).to_have_count(len(products), timeout=5000)



# @allure.epic("E-Commerce App")
# @allure.feature("Contact Info")
# @allure.story("Popup Handling")
# @allure.severity(allure.severity_level.MINOR)
# @allure.title("Extract email address from popup window")
# @pytest.mark.order(3)

# def test_extract_email_from_popup(login):
#     # Open popup
#     with login.expect_popup() as popup_info:
#         login.locator(".blinkingText").wait_for(state="visible", timeout=5000)
#         login.locator(".blinkingText").click()
#
#     popup = popup_info.value
#     popup.wait_for_load_state()
#
#     # Extract email from text
#     text = popup.locator(".red").text_content()
#
#     try:
#         email = text.split("at")[1].strip().split(" ")[0]
#     except IndexError:
#         pytest.fail("Failed to extract email from popup text")
#
#     print("Extracted Email:", email)
#     assert "@" in email and "." in email  # Basic email sanity check
