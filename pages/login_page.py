class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_label("Username:")
        self.password_input = page.get_by_label("Password:")
        self.role_dropdown = page.get_by_role("combobox")
        self.terms_checkbox = page.locator("#terms")
        self.signin_button = page.get_by_role("button", name="Sign In")

    def login(self, username, password, role="Teacher", accept_terms=True):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.role_dropdown.select_option(role)
        if accept_terms:
            self.terms_checkbox.check()
        self.signin_button.click()




23456


