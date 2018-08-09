from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os
from pages.home.login_page import LoginPage


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        driverLocation = "C:\\webdrivers\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@gmail.com", "abcabc")

        userIcon = driver.find_element(By.CSS_SELECTOR, ".gravatar")

        if userIcon is not None:
            print("Login sucsess")
        else:
            print("Failed")
