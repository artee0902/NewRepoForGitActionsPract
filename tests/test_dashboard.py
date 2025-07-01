import pytest
from pages.dashboard_page import DashboardPage

def test_dashboard_header_visible(login):
    dashboard = DashboardPage(login)
    assert dashboard.get_header_text() == "Dashboard"

def test_logout_functionality(login):
    dashboard = DashboardPage(login)
    dashboard.logout()
    assert "login" in login.url.lower()

# def test_invalid_url_access_redirection(login):
#     login.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewAdminModule")
#     assert "dashboard" in login.url.lower()  # Or you can check for access denied message


