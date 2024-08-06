from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class Test_Login:
    def test_Login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("madhukumarhm605@gmail.com")
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Madhu@1234")
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        print("test passed")
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed(),"login Failed try again"


    def test_Login_with_Invalid_credentials(self):
        #self.driver.get("https://tutorialsninja.com/demo/index.php?")
        self.driver.find_element(By.XPATH,"//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys(self.genereate_email_with_timestamp())
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Madhu@1234")
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        exp_Msg ="Warning: No match for E-Mail Address and/or Password."
        print("invalid test case")
        assert self.driver.find_element(By.XPATH,"//div[contains(text(),'Warning:')]").text == exp_Msg,"login Succesfull with invalid credentials test case failed try again"

    def test_Login_with_valid_Email_and_Invalid_Password(self):
        #self.driver.get("https://tutorialsninja.com/demo/index.php?")
        self.driver.find_element(By.XPATH,"//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("madhukumarhm605@gmail.com")
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Madhu@1734")
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        exp_Msg ="Warning: No match for E-Mail Address and/or Password."
        print("invalid test case")
        assert self.driver.find_element(By.XPATH,"//div[contains(text(),'Warning:')]").text.__contains__(exp_Msg),"login Succesfull with invalid credentials test case failed try again"

    def test_Login_without_credentials(self):
        #self.driver.get("https://tutorialsninja.com/demo/index.php?")
        self.driver.find_element(By.XPATH,"//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("")
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("")
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        exp_Msg ="Warning: No match for E-Mail Address and/or Password."
        print("invalid test case")
        assert self.driver.find_element(By.XPATH,"//div[contains(text(),'Warning:')]").text.__contains__(exp_Msg),"login Succesfull with invalid credentials test case failed try again"

    def genereate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "madhu"+time_stamp+"@gamil.com"