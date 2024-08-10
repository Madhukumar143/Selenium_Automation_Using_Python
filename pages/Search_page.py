from pages.Base_page import Basepage

class Search_page(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_xpath = "//a[contains(text(),'HP')]"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_valid_hp_product(self):
        return self.check_display_status("valid_hp_product_xpath", self.valid_hp_product_xpath)

    def retrieve_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath", self.no_product_message_xpath)
