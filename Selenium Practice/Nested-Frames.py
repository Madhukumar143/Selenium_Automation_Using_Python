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
driver.implicitly_wait(10)

driver.get("https://letcode.in/frame")
driver.switch_to.frame("firstFr")
driver.find_element(By.NAME,"fname")
driver.switch_to.frame("googlefcPresent")
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='has-background-white']"))
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='googlefcPresent']"))

driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys("Madhu virat")

time.sleep(3)




