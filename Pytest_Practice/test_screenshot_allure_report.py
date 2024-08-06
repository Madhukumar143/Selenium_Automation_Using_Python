import time

import allure
import pytest
from allure_commons.types import AttachmentType
# use this command pytest parallel_execution.py -n 3
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#to run pytest files with allure run this command in terminal pytest test_screenshot_allure_report.py --alluredir="./reports"


# open cmd and run this command for geberating allure report allure serve "./reports" run this in CMD
@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class TestSearch:
    def test_tut_ninja_valid_search(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        if self.driver.find_element(By.LINK_TEXT, "HP LP3965").is_displayed():
            print("Found the correct item")
            #allure.attach(self.driver.get_screenshot_as_png(),name="Valid Search",attachment_type=AttachmentType.PNG)
        else:
            print("test case failed")
            #allure.attach(self.driver.get_screenshot_as_png(), name="Valid Search failed", attachment_type=AttachmentType.PNG)

    def test_tut_ninja_invalid_search(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        exp_text = "There is no product that matches the search criteria."
        if self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text == exp_text:
            print("invalid search no search result")
            #allure.attach(self.driver.get_screenshot_as_png(), name="Valid Search failed",attachment_type=AttachmentType.PNG)
        else:
            print("Search result found")
            #allure.attach(self.driver.get_screenshot_as_png(), name="Valid Search failed",attachment_type=AttachmentType.PNG)