import pytest
import allure
from pages.dashboard_page import DashboardPage
from playwright.sync_api import expect

@allure.epic("OrangeHRM Dashboard")
@allure.feature("Profile Dropdown")
@allure.story("Verify dropdown options are visible")
@allure.title("Check all expected options appear in profile dropdown")
@allure.severity(allure.severity_level.NORMAL)
def test_profile_dropdown_visible_options(login):
    dashboard = DashboardPage(login)
    dashboard.open_profile_dropdown()
    options = dashboard.get_dropdown_options()
    assert "About" in options
    assert "Support" in options
    assert "Change Password" in options
    assert "Logout" in options

@allure.epic("OrangeHRM Dashboard")
@allure.feature("Profile Dropdown")
@allure.story("About popup validation")
@allure.title("Verify About modal opens and displays correct title")
@allure.severity(allure.severity_level.CRITICAL)
def test_about_popup_content(login):
    dashboard = DashboardPage(login)
    dashboard.open_profile_dropdown()
    login.locator("a:has-text('About')").wait_for(state="visible", timeout=5000)
    dashboard.click_about()
    modal = login.locator("div[role='document']")
    expect(modal).to_be_visible(timeout=7000)
    modal_title = modal.locator("h6")
    expect(modal_title).to_have_text("About")
    login.locator("button:has-text('×')").click()
    expect(modal).not_to_be_visible(timeout=5000)

@allure.epic("OrangeHRM Dashboard")
@allure.feature("Profile Dropdown")
@allure.story("Support page redirection")
@allure.title("Verify clicking Support navigates to Help URL")
@allure.severity(allure.severity_level.NORMAL)
def test_support_page_navigation(login):
    dashboard = DashboardPage(login)
    dashboard.click_support()
    expect(login).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/help/support")

@allure.epic("OrangeHRM Dashboard")
@allure.feature("Profile Dropdown")
@allure.story("Change Password functionality")
@allure.title("Verify Change Password navigates to Update Password page")
@allure.severity(allure.severity_level.NORMAL)
def test_change_password_page(login):
    dashboard = DashboardPage(login)
    dashboard.click_change_password()
    heading = login.locator("h6.oxd-text.oxd-text--h6.orangehrm-main-title")
    expect(heading).to_have_text("Update Password")
