from tests.pages.register_page import RegisterPage

def test_register_with_valid_data(page, base_url, random_string):
    rp = RegisterPage(page, base_url)
    rp.goto()
    username = "user_" + random_string(6)
    email = f"{username}@example.com"
    password = "StrongP@ssw0rd123"
    rp.register(username, email, password)
    success = rp.get_success_text()
    assert success, "Expected success message after registration"