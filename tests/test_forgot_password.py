import pytest
from pages.forgot_password_page import ForgotPasswordPage

@pytest.mark.parametrize(
    "email",
    [
        "test@example.com",   # valid email
        "wrongemail",         # invalid email
    ]
)
def test_forgot_password(driver, email):
    forgot = ForgotPasswordPage(driver)
    forgot.open()
    forgot.submit_email(email)

    message = forgot.get_message().lower()

    # Application always shows confirmation
    assert "forgot password" in message or "retrieve" in message
