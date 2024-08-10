import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from pages.Home_page import Home_page
from pages.Search_page import Search_page

@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class Test_Search():
    def test_Valid_search(self):
        home_page = Home_page(self.driver)
        search_page = home_page.Search_for_a_product("HP")#we are opening search page in this function
        assert search_page.display_status_of_valid_hp_product(),"HP 3605 not found"

    def test_Invalid_search(self):
        home_page = Home_page(self.driver)
        search_page = home_page.Search_for_a_product("Honda")
        exp_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(exp_text),"Search result found for invalid search"

    def test_Without_search(self):
        home_page = Home_page(self.driver)
        search_page = home_page.Search_for_a_product("")
        exp_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(exp_text),"Search result found for No search"
