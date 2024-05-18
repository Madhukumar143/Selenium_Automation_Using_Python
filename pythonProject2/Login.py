import time

from datetime import date, datetime

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

#to print the time of test run
datetime = datetime.now()
print(datetime)

# # Enter the User-name and password Manually
Email_ID= input("enter the email id")
Password =input("enter the password")

Ch_Options = Options()
driver = webdriver.Chrome(Ch_Options)
Ch_Options.add_argument("--incognito")

# to stop the browser automatically stopping the application
driver.get("https://development.d3rbslpj3wyrjv.amplifyapp.com/auth/login")
# Maximize the window opened
driver.maximize_window()
time.sleep(2)

def Login():

#Enter User Credentials
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(Email_ID)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(Password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
    time.sleep(1)
    exp_url = "https://development.d3rbslpj3wyrjv.amplifyapp.com/dashboard?ap=AT00307"

    if exp_url != driver.current_url:
        Alert_Text = driver.find_element(By.XPATH, "//div[@class='p-toast-detail ng-tns-c3213092237-3']").text
        print(Alert_Text)
        print("Test case Failed - Raise the bug")
        driver.get_screenshot_as_file("D:\\Automation\\TestFail.PNG")

    else:
        print("User Logged in Successfully")
        driver.get_screenshot_as_file("D:\\Automation\\TestPass.PNG")
Login()