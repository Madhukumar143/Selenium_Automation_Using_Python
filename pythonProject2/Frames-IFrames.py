import time

from datetime import date, datetime

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

datetime = datetime.now()
print(datetime)
ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
'''Ch_Options = Options()
driver = webdriver.Chrome(Ch_Options)
driver.implicitly_wait(10)
Ch_Options.add_argument("--incognito")'''

# to stop the browser automatically stopping the application
'''Ch_Options.add_experimental_option('detach',True)'''
driver.get('https://chercher.tech/practice/frames')
# Maximize the window opened
driver.maximize_window()
time.sleep(2)

#Switch to frame
driver.switch_to.frame('iamframe')


#switch to nested frame
driver.switch_to.frame('frame3')
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.switch_to.parent_frame()
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Madhu Virat")
# Come back to main Window
driver.switch_to.default_content()

#switch to frame
driver.switch_to.frame('frame2')

#drop Down Select
a = Select(driver.find_element(By.XPATH, "//select[@class='col-lg-3']"))

#Select value by visibility text
a.select_by_visible_text('Avatar')
time.sleep(3)

