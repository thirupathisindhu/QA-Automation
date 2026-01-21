import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("student", "Password123", True),
        ("student", "wrongpass", False),
        ("wronguser", "Password123", False)
    ]
)
def test_login(driver, username, password, expected):
    login = LoginPage(driver)
    login.open()
    login.login(username, password)

    if expected:
        assert login.is_login_successful()
    else:
        error = login.get_error_message()
        assert error != ""
