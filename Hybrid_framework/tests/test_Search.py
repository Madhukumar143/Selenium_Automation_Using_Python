import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class Test_Search:
    def test_Valid_search(self):
        (self.
         driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("HP"))
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        if self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed():
            print("Found the correct item")
            # allure.attach(self.driver.get_screenshot_as_png(),name="Valid Search",attachment_type=AttachmentType.PNG)
        else:
            print("test case failed searched item not found")
            # allure.attach(self.driver.get_screenshot_as_png(), name="Valid Search failed", attachment_type=AttachmentType.PNG)


    def test_Invalid_search(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        exp_text = "There is no product that matches the search criteria."
        if self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text == exp_text:
            print("invalid search no search result")
            # allure.attach(self.driver.get_screenshot_as_png(), name="Valid Search failed",attachment_type=AttachmentType.PNG)
        else:
            print("Search result found for invalid search")
            # allure.attach(self.driver.get_screens

    def test_Without_search(self):

        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        exp_text = "There is no product that matches the search criteria."
        assert (self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p")).text ==exp_text,"Search result found for No search"
            # print("invalid search no search result")
            # allure.attach(self.driver.get_screenshot_as_png(), name="Valid Search failed",attachment_type=AttachmentType.PNG)
        # else:
        #
        #allure.attach(self.driver.get_screens