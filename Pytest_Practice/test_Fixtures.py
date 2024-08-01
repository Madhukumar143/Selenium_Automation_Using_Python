import pytest

"""@pytest.fixture()
def setup_and_teardown():
    print("Launch browser")
    print("open Application URL in Browser")
    yield
    print("Logout from the application")
    print("Close the browser")"""

def test_login_with_valid_credentials(setup_and_teardown):
    print("test Fixtures")

def test_login_with_invalid_credentials(setup_and_teardown):
    print("test Fixtures")