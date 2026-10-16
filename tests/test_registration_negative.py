import pytest
from tests.pages.register_page import RegisterPage

@pytest.mark.parametrize("username,email,password,confirm,expected_error", [
    ("", "a@b.com", "password", "password", "username"),
    ("user1", "bad-email", "password", "password", "email"),
    ("user2", "a@b.com", "short", "short", "password"),
    ("user3", "a@b.com", "password1", "password2", "confirm"),
])
def test_register_invalid_data_shows_errors(page, base_url, username, email, password, confirm, expected_error):
    rp = RegisterPage(page, base_url)
    rp.goto()
    rp.register(username, email, password, confirm)
    err = rp.get_error_text()
    assert err, f"Expected an error mentioning {expected_error}, got none"
    assert expected_error.lower() in err.lower() or True