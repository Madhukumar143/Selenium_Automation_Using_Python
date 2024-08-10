import pytest
from selenium.webdriver.common.by import By

from pages.Base_page import Basepage

class Login_page(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    login_email_xpath = "//input[@name='email']"
    login_password_xpath = "//input[@name='password']"
    login_button_xpath = "//input[@type='submit']"
    login_confirmation_link_text = "Edit your account information"
    warning_msg_xpath_for_invalid_login = "//div[contains(text(),'Warning:')]"

    def send_login_email_and_password(self, user_email, user_password):
        self.type_into_element(user_email, "login_email_xpath", self.login_email_xpath)
        self.type_into_element(user_password, "login_password_xpath", self.login_password_xpath)

    def click_on_login_button(self):
        self.element_click("login_button_xpath", self.login_button_xpath)

    def login_confirmation(self):
        return self.check_display_status("login_confirmation_link_text", self.login_confirmation_link_text)

    def Invalid_login_confirmation(self):
        return self.check_display_status("warning_msg_xpath_for_invalid_login", self.warning_msg_xpath_for_invalid_login)
