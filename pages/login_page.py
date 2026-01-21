from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    URL = "https://practicetestautomation.com/practice-test-login/"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "submit")
    ERROR_MSG = (By.ID, "error")
    LOGOUT_BTN = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_error_message(self):
        try:
            error = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MSG)
            )
            return error.text
        except:
            return ""

    def is_login_successful(self):
        return len(self.driver.find_elements(*self.LOGOUT_BTN)) > 0
