import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#to print the time of test run
datetime = datetime.now()
print(datetime)

ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.implicitly_wait(15)
'''Ch_Options = Options()
driver = webdriver.Chrome(Ch_Options)
driver.implicitly_wait(10)
Ch_Options.add_argument("--incognito")'''

# to stop the browser automatically stopping the application
#Ch_Options.add_experimental_option('detach',True)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# Maximize the window opened
driver.maximize_window()
#print(driver.current_window_handle)
driver.find_element(By.XPATH, "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']").click()
time.sleep(6)
a=driver.window_handles
# Approach 1
'''Parent_window_id = a[0]
Child_window_id = a[1]
driver.switch_to.window(Parent_window_id)
print("parent title is ",driver.title)
time.sleep(6)
driver.switch_to.window(Child_window_id)
print("child title is ",driver.title)
time.sleep(5)'''

# Approach 2 (closing window by title of window
for winid in a:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM | LinkedIn":
        driver.close()
time.sleep(4)