import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Hybrid_framework.tests.Basetest import Base_test
from Hybrid_framework.tests.utilities import Excelutils
from pages.Home_page import Home_page

class Test_Login(Base_test):
    @pytest.mark.parametrize("email_address,password",Excelutils.Extract_Excel_data("Excel_files/Practice.xlsx", "Sheet1"))
    def test_Login_with_valid_credentials(self,email_address,password):
        home_page = Home_page(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.send_login_email_and_password(email_address,password)
        login_page.click_on_login_button()
        time.sleep(2)
        assert login_page.login_confirmation(),"login Failed try again"

    def test_Login_with_Invalid_credentials(self):
        home_page = Home_page(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.send_login_email_and_password(self.generate_email_with_timestamp(), "Madhu@1234")
        login_page.click_on_login_button()
        #exp_Msg ="Warning: No match for E-Mail Address and/or Password."
        assert login_page.Invalid_login_confirmation(),"login Succesfull with invalid credentials test case failed try again"

    def test_Login_with_valid_Email_and_Invalid_Password(self):
        home_page = Home_page(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.send_login_email_and_password("madhukumarhm605@gmail.com","madhu@1234")
        login_page.click_on_login_button()
        #exp_Msg ="Warning: No match for E-Mail Address and/or Password."
        assert login_page.Invalid_login_confirmation(),"login Succesfull with invalid credentials test case failed try again"

    def test_Login_without_credentials(self):
        home_page = Home_page(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.send_login_email_and_password("madhukumarhm605@gmail.com", "madhu@1234")
        login_page.click_on_login_button()
        # exp_Msg ="Warning: No match for E-Mail Address and/or Password."
        assert login_page.Invalid_login_confirmation(),"login Succesfull with invalid credentials test case failed try again"

    # def generate_email_with_timestamp(self):  # Fixed spelling of 'generate'
    #     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    #     return "madhu" + time_stamp + "@gmail.com"  # Corrected the spelling of 'gmail'
