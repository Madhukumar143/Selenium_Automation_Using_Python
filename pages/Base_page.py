from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Basepage:

    def __init__(self,driver):
        self.driver = driver

    def type_into_element(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def check_display_status(self,locator_name,locator_value):
        return self.get_element(locator_name,locator_value)

    def retrieve_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    def get_element(self, locator_name, locator_value):
        element = None
        try:
            if locator_name.__contains__("_id"):
                element = self.driver.find_element(By.ID, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("_name"):
                element = self.driver.find_element(By.NAME, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("_xpath"):
                element = self.driver.find_element(By.XPATH, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("link_text"):
                element = self.driver.find_element(By.LINK_TEXT, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("_class_name"):
                element = self.driver.find_element(By.CLASS_NAME, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_name.__contains__("_css"):
                element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
        except NoSuchElementException:
            return False
