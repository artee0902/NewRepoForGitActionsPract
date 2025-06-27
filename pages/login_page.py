class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("input#username")
        self.password_input = page.locator("input#password")
        self.role_dropdown = page.locator("select.form-control")
        self.terms_checkbox = page.locator("#terms")
        self.signin_button = page.locator("#signInBtn")

    def login(self, username, password, role="Teacher", accept_terms=True):
        self.username_input.wait_for(state="visible", timeout=10000)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.role_dropdown.select_option(label=role)
        if accept_terms:
            self.terms_checkbox.check()
        self.signin_button.click()
