import time
from datetime import date, datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

datetime = datetime.now()
print(datetime)
ch_option =Options()
driver = webdriver.Chrome(ch_option)
driver.implicitly_wait(3)

driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
left_text = driver.find_element(By.XPATH,"//body").text
print(left_text)
driver.switch_to.parent_frame()
#Middle frame
driver.switch_to.frame("frame-middle")
Middle_text = driver.find_element(By.XPATH,"//body").text
print(Middle_text)
driver.switch_to.parent_frame()
#Right_Frame
driver.switch_to.frame("frame-right")
Right_text = driver.find_element(By.XPATH,"//body").text
print(Right_text)

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
bottom = driver.find_element(By.XPATH,"//body").text
print(bottom)


time.sleep(3)
