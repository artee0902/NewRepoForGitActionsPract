from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")
        self.profile_dropdown = page.locator("span.oxd-userdropdown-tab")
        self.logout_button = page.locator("a[href='/web/index.php/auth/logout']")
        self.dropdown_items = page.locator("ul.oxd-dropdown-menu > li > a")
        self.about_button = page.locator("a:has-text('About')")
        self.support_button = page.locator("a:has-text('Support')")
        self.change_password_button = page.locator("a:has-text('Change Password')")

    def get_header_text(self):
        return self.header.text_content()

    def logout(self):
        self.profile_dropdown.click()
        self.logout_button.click()

    def open_profile_dropdown(self):
        self.profile_dropdown.click()

    def get_dropdown_options(self):
        self.open_profile_dropdown()
        return [item.inner_text() for item in self.dropdown_items.all()]

    def click_about(self):
        self.open_profile_dropdown()
        self.about_button.click()

    def click_support(self):
        self.open_profile_dropdown()
        self.support_button.click()

    def click_change_password(self):
        self.open_profile_dropdown()
        self.change_password_button.click()

