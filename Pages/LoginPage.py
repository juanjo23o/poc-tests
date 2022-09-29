from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class LoginPage(BasePage):

    """By locators"""
    EMAIL = (By.ID, "loginFormEmailInput")
    PASSWORD = (By.ID, "loginFormPasswordInput")
    LOGIN_BUTTON = (By.XPATH , "//span[text()='Login']")
    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions for login page"""

    """this is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """This is used to login to app"""
    def do_login(self, username, password):
        self.send_keys(self.EMAIL, username)
        self.send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)