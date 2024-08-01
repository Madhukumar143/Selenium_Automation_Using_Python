import pytest
@pytest.fixture()# we can use autouse, scope as parameters here
def setup_and_teardown():
    print("Launch browser")
    print("open Application URL in Browser")
    yield
    print("Logout from the application")
    print("Close the browser")