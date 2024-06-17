import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://omayo.blogspot.com/")
time.sleep(2)
driver.refresh()
driver.maximize_window()
#driver.find_element(By.XPATH," any element of the form").submit() # submit any form

driver.find_element(By.LINK_TEXT,"onlytestingblog").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()