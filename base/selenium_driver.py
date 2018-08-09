from selenium.webdriver.common.by import By

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locator_type):
        if locator_type == "CSS":
            return By.CSS_SELECTOR
        elif locator_type == "XPATH":
            return By.XPATH
        elif locator_type == "LINK":
            return By.LINK_TEXT
        elif locator_type == "ID":
            return By.ID
        elif locator_type == "NAME":
            return By.NAME

    def findElement(self, locator_type, locator_value):
        element = None
        try:
            locator_type = locator_type.upper()
            byType = self.getByType(locator_type)
            element = self.driver.find_element (byType, locator_value)
        except:
            print("Element not found" + locator_value)
        return element

    def click_element(self, locator_type, locator_value):
        element = self.findElement(locator_type, locator_value)
        element.click()

    def sentKeys(self, locator_type, locator_value, data):
        element = self.findElement(locator_type, locator_value)
        element.sent_keys(data)

    def isElementPresent(self, locator_type, locator_value):
        element = self.findElement(locator_type, locator_value).is_displayed()
        return element
