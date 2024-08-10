from datetime import datetime

import pytest

from Hybrid_framework.tests.Basetest import Base_test
from pages.Home_page import Home_page

@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class Test_register(Base_test):
    def test_register_with_mandatory_fields(self):
        home_page = Home_page(self.driver)
        register_page =  home_page.navigate_to_register_page()
        register_page.enter_firstname_lastname("Madhu kumar","H M")
        register_page.enter_email_telephone(self.generate_email_with_timestamp(),"8296790417")
        register_page.enter_password_and_confirm_password("mad@1234","mad@1234")
        register_page.privacy_policy_selection()
        register_page.click_continue_button_to_register()
        exp_text = "Your Account Has Been Created!"
        assert register_page.retrieve_text_after_registering().__contains__(exp_text), "Something went wrong, account not created/registered"

    def test_register_with_all_fields(self):
        home_page = Home_page(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.enter_firstname_lastname("Madhu kumar", "H M")
        register_page.enter_email_telephone(self.generate_email_with_timestamp(), "8296790417")
        register_page.enter_password_and_confirm_password("mad@1234", "mad@1234")
        register_page.news_letter_selection("yes")
        register_page.privacy_policy_selection()
        register_page.click_continue_button_to_register()
        exp_text = "Your Account Has Been Created!"
        assert register_page.retrieve_text_after_registering().__contains__(exp_text), "Something went wrong, account not created/registered"

    def test_register_with_duplicate_email(self):
        home_page = Home_page(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.enter_firstname_lastname("Madhu kumar", "H M")
        register_page.enter_email_telephone("madhukumarhm605@gmail.com", "8296790417")
        register_page.enter_password_and_confirm_password("mad@1234", "mad@1234")
        register_page.privacy_policy_selection()
        register_page.click_continue_button_to_register()
        exp_text = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_warning_msg_for_already_registered_mail().__contains__(exp_text), "Warning: E-Mail Address is already registered!"

    def test_register_without_entering_any_data(self):
        home_page = Home_page(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.enter_firstname_lastname("", "")
        register_page.enter_email_telephone("", "")
        register_page.enter_password_and_confirm_password("", "")
        register_page.click_continue_button_to_register()
        exp_text = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_warning_msg_for_notselected_privacyPolicy().__contains__(exp_text), "Warning: You must agree to the Privacy Policy!"
        Exp_Warn_Fname = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_warning_msg_for_empty_firstname().__contains__(Exp_Warn_Fname), "Entered first name is correct"
        Exp_Warn_Lname = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_warning_msg_for_empty_lastname().__contains__(Exp_Warn_Lname), "Entered last name is correct"
        Exp_Warn_Email = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_warning_msg_for_empty_email().__contains__(Exp_Warn_Email), "Entered email is correct"
        Exp_Warn_Telephone = "Telephone must be between 3 and 32 characters!"
        assert register_page.retrieve_warning_msg_for_empty_telephone_number().__contains__(Exp_Warn_Telephone), "Entered number is correct"
        Exp_Warn_Password = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_warning_msg_for_empty_password().__contains__(Exp_Warn_Password), "Entered password is correct"

    # def generate_email_with_timestamp(self):  # Fixed spelling of 'generate'
    #     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    #     return "madhu" + time_stamp + "@gmail.com"  # Corrected the spelling of 'gmail'