import time
from datetime import date, datetime
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#to print the time of test run
datetime = datetime.now()
print(datetime)

# # Enter the User-name and password Manually
# EmailId = "teacher@giis.com"#input("enter the email id")
# password = "Test@1234"#input("enter the password")

ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
'''Ch_Options = Options()
driver = webdriver.Chrome(Ch_Options)
driver.implicitly_wait(10)
Ch_Options.add_argument("--incognito")'''

# to stop the browser automatically stopping the application
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# Maximize the window opened
driver.maximize_window()
time.sleep(2)

def Login():

#Enter User Credentials
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")

    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    if exp_url != driver.current_url:
        print("Test case Failed - Raise the bug")
        driver.get_screenshot_as_file("D:\\Automation\\TestFail.PNG")

    else:
        print("User Logged in Successfully")
        driver.get_screenshot_as_file("D:\\Automation\\TestPass.PNG")

