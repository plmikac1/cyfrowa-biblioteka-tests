import pytest
from tests.pages.register_page import RegisterPage

@pytest.mark.parametrize("length", [1, 2, 10, 50, 100, 255])
def test_username_length_boundary(page, base_url, random_string, length):
    rp = RegisterPage(page, base_url)
    rp.goto()
    username = random_string(length)
    email = f"{username[:20]}@example.com"
    password = "BoundaryP@ss1"
    rp.register(username, email, password)
    err = rp.get_error_text()
    if err:
        assert "length" in err.lower() or "too" in err.lower() or "maximum" in err.lower()
    else:
        success = rp.get_success_text()
        assert success, "Expected success for allowed boundary or error for too long input"

def test_special_characters_in_username(page, base_url, random_string):
    rp = RegisterPage(page, base_url)
    rp.goto()
    username = "user!@#$%^&*()-_=+[]{};:,.<>/?`~"
    email = "special@example.com"
    password = "SpecP@ssw0rd"
    rp.register(username, email, password)
    assert rp.get_error_text() or rp.get_success_text()