from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class Base_test():
    def generate_email_with_timestamp(self):  # Fixed spelling of 'generate'
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "madhu" + time_stamp + "@gmail.com"  # Corrected the spelling of 'gmail'
