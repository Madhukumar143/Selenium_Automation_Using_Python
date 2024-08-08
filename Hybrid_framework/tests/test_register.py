from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class Test_register:
    def test_register_with_mandatory_fields(self):
        #self.driver.get("https://tutorialsninja.com/demo/index.php")
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Madhu kumar")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("H M")
        # Use self to call the method
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("1234567890")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("mad@1234")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("mad@1234")
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        exp_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(exp_text), "Something went wrong, account not created/registered"

    def test_register_with_all_fields(self):
        #self.driver.get("https://tutorialsninja.com/demo/index.php")
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Madhu kumar")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("H M")
        # Use self to call the method
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("1234567890")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("mad@1234")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("mad@1234")
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        exp_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(exp_text), "Something went wrong, account not created/registered"

    def test_register_with_duplicate_email(self):
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.get("https://tutorialsninja.com/demo/index.php")
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Madhu kumar")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("H M")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("madhukumarhm605@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("1234567890")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("mad@1234")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("mad@1234")
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        exp_text = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(exp_text), "Warning: E-Mail Address is already registered!"

    def test_register_without_entering_any_data(self):
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        #driver.get("https://tutorialsninja.com/demo/index.php")
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        exp_text = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(exp_text), "Warning: You must agree to the Privacy Policy!"
        Exp_Warn_Fname = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__contains__(Exp_Warn_Fname), "Entered first name is correct"
        Exp_Warn_Lname = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__contains__(Exp_Warn_Lname), "Entered last name is correct"
        Exp_Warn_Email = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@name='email']/following-sibling::div").text.__contains__(Exp_Warn_Email), "Entered email is correct"
        Exp_Warn_Telephone = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@name='telephone']/following-sibling::div").text.__contains__(Exp_Warn_Telephone), "Entered number is correct"
        Exp_Warn_Password = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@name='password']/following-sibling::div").text.__contains__(Exp_Warn_Password), "Entered password is correct"

    def generate_email_with_timestamp(self):  # Fixed spelling of 'generate'
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "madhu" + time_stamp + "@gmail.com"  # Corrected the spelling of 'gmail'
