from selenium.webdriver.common.by import By

class ForgotPasswordPage:

    EMAIL = (By.ID, "email")
    SUBMIT_BTN = (By.ID, "form_submit")
    MESSAGE = (By.ID, "content")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/forgot_password")

    def submit_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def get_message(self):
        return self.driver.find_element(*self.MESSAGE).text
