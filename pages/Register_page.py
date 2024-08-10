from selenium.webdriver.common.by import By

from pages.Base_page import Basepage


class Register_page(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    firstname_xpath = "//input[@name='firstname']"
    lastname_xpath = "//input[@name='lastname']"
    email_xpath = "//input[@name='email']"
    telephone_xpath = "//input[@name='telephone']"
    password_xpath = "//input[@name='password']"
    confirm_password_xpath = "//input[@name='confirm']"
    privacy_policy_check_box_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    news_letter_radio_button_xpath_for_yes = "//label[normalize-space()='Yes']"
    news_letter_radio_button_xpath_for_No = "//label[normalize-space()='No']"
    warning_msg_xpath_for_already_registered_mail ="//div[@id='account-register']/div[1]"
    Exp_text_xpath = "//div[@id='content']/h1"
    warning_msg_xpath_for_firstname = "//input[@id='input-firstname']/following-sibling::div"
    warning_msg_xpath_for_privacypolicy = "//div[@id='account-register']/div[1]"
    warning_msg_xpath_for_lastname = "//input[@id='input-lastname']/following-sibling::div"
    warning_msg_xpath_for_email = "//input[@name='email']/following-sibling::div"
    warning_msg_xpath_for_telephone = "//input[@name='telephone']/following-sibling::div"
    warning_msg_xpath_for_password ="//input[@name='password']/following-sibling::div"

    def enter_firstname_lastname(self,fname,lname):
        self.type_into_element(fname,"firstname_xpath",self.firstname_xpath)
        self.type_into_element(lname,"lastname_xpath", self.lastname_xpath)

    def enter_email_telephone(self,email,telephone):
        self.type_into_element(email,"email_xpath", self.email_xpath)
        self.type_into_element(telephone, "telephone_xpath",self.telephone_xpath)

    def enter_password_and_confirm_password(self,password,confirm_password):
        self.type_into_element(password, "password_xpath",self.password_xpath)
        self.type_into_element(confirm_password,"confirm_password_xpath", self.confirm_password_xpath)

    def news_letter_selection(self,value):
        if value=="yes"or"Yes":
            self.element_click("news_letter_radio_button_xpath_for_yes",self.news_letter_radio_button_xpath_for_yes)
        elif value=="no"or"NO":
            self.element_click("news_letter_radio_button_xpath_for_No",self.news_letter_radio_button_xpath_for_No)
    def privacy_policy_selection(self):
        self.element_click("privacy_policy_check_box_xpath",self.privacy_policy_check_box_xpath)

    def click_continue_button_to_register(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)

    def retrieve_text_after_registering(self):
        return self.retrieve_element_text("Exp_text_xpath",self.Exp_text_xpath)

    def retrieve_warning_msg_for_already_registered_mail(self):
        return self.retrieve_element_text("warning_msg_xpath_for_already_registered_mail",self.warning_msg_xpath_for_already_registered_mail)

    def retrieve_warning_msg_for_empty_firstname(self):
        return self.retrieve_element_text("warning_msg_xpath_for_firstname",self.warning_msg_xpath_for_firstname)

    def retrieve_warning_msg_for_empty_lastname(self):
        return self.retrieve_element_text("warning_msg_xpath_for_lastname",self.warning_msg_xpath_for_lastname)

    def retrieve_warning_msg_for_empty_email(self):
        return self.retrieve_element_text("warning_msg_xpath_for_email",self.warning_msg_xpath_for_email)

    def retrieve_warning_msg_for_empty_telephone_number(self):
        return self.retrieve_element_text("warning_msg_xpath_for_telephone",self.warning_msg_xpath_for_telephone)

    def retrieve_warning_msg_for_empty_password(self):
        return self.retrieve_element_text("warning_msg_xpath_for_password",self.warning_msg_xpath_for_password)

    def retrieve_warning_msg_for_notselected_privacyPolicy(self):
        return self.retrieve_element_text("warning_msg_xpath_for_privacypolicy",self.warning_msg_xpath_for_privacypolicy)











