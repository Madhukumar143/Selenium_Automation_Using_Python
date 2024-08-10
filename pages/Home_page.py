from selenium.webdriver.common.by import By

from pages.Base_page import Basepage
from pages.Login_page import Login_page
from pages.Register_page import Register_page
from pages.Search_page import Search_page


class Home_page(Basepage):

    def __init__(self,driver):
        super().__init__(driver)

    search_box_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_drop_menu_xpath = "//span[contains(text(),'My Account')]"
    login_option_link_text = "Login"
    register_option_link_text = "Register"


    def Search_for_a_product(self,product_name):
        self.type_into_element(product_name,"search_box_xpath",self.search_box_xpath)
        self.element_click("search_button_xpath",self.search_button_xpath)
        # self.driver.find_element(By.XPATH, self.search_box_xpath).clear()
        # self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(product_name)
        # self.driver.find_element(By.XPATH,self.search_button_xpath).click()
        return Search_page(self.driver)

    def navigate_to_login_page(self):
        self.element_click("my_account_drop_menu_xpath",self.my_account_drop_menu_xpath)
        self.element_click("login_option_link_text",self.login_option_link_text)
        return Login_page(self.driver)

    def navigate_to_register_page(self):
        self.element_click("my_account_drop_menu_xpath",self.my_account_drop_menu_xpath,)
        self.element_click("register_option_link_text",self.register_option_link_text)
        return Register_page(self.driver)
