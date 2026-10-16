class RegisterPage:
    def __init__(self, page, base_url):
        self.page = page
        self.url = f"{base_url}/register"
        # Update selectors to match your page
        self.username = 'input[name="username"]'
        self.email = 'input[name="email"]'
        self.password = 'input[name="password"]'
        # some apps use confirm_password or password_confirm
        self.password_confirm = 'input[name="password_confirm"], input[name="confirm_password"]'
        self.submit = 'button[type="submit"]'
        self.success_message = '.flash-success, .alert-success, .success'
        self.error_message = '.error, .alert-danger, .field-error'

    def goto(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    def register(self, username, email, password, confirm=None):
        # clear fields before fill to be resilient
        try:
            self.page.fill(self.username, "")
        except Exception:
            pass
        self.page.fill(self.username, username)
        self.page.fill(self.email, email)
        self.page.fill(self.password, password)
        if confirm is None:
            confirm = password
        # Some sites may not have a confirm field; ignore errors
        try:
            self.page.fill(self.password_confirm, confirm)
        except Exception:
            pass
        self.page.click(self.submit)
        # wait for either success or error
        self.page.wait_for_load_state("networkidle")

    def get_success_text(self):
        el = self.page.query_selector(self.success_message)
        return el.inner_text().strip() if el else ""

    def get_error_text(self):
        el = self.page.query_selector(self.error_message)
        return el.inner_text().strip() if el else ""