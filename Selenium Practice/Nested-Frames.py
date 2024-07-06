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
driver.find_element(By.NAME,"fname").send_keys("Madhu")
driver.find_element(By.XPATH,"//input[@name='lname']").send_keys("Kumar")
child_Frame = driver.find_element(By.XPATH,"//iframe[@class='has-background-white']")
driver.switch_to.frame(child_Frame)
driver.find_element(By.NAME,"email").send_keys("madhu@gmail.com")
driver.find_element(By.NAME,"email").clear()
driver.switch_to.parent_frame()
driver.find_element(By.NAME,"fname").clear()
driver.find_element(By.XPATH,"//input[@name='lname']").clear()
#switch from frame level to page level
driver.switch_to.default_content()

main_text= driver.find_element(By.XPATH,"//div[@class='hero-body']//h1").text
print(main_text)

'''driver.find_element(By.NAME,"fname")
driver.switch_to.frame("googlefcPresent")
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='has-background-white']"))
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='googlefcPresent']"))

driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys("Madhu virat")

time.sleep(3)'''




