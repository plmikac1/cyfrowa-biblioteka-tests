import os
import pytest

# pytest-playwright provides a `page` fixture you can use directly in tests.
# BASE_URL should point to your running application.
@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost:8000")

@pytest.fixture
def random_string():
    import random, string
    def _gen(length=8):
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))
    return _gen