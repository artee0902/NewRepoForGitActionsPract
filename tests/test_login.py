import pytest
from pages.login_page import LoginPage

def test_login_success(login):
    assert "dashboard" in login.url.lower()
