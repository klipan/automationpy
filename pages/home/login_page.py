from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.click_element("LINK", self._login_link)

    def enterEmail(self, email):
        self.sentKeys("ID", self._email_field, email)

    def enterPassword(self, password):
        self.sentKeys("ID", self._password_field, password)

    def clickLoginButton(self):
        self.click_element("NAME", self._login_button)

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
