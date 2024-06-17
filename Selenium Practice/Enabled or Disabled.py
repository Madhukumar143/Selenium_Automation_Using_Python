import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

#for button two
if driver.find_element(By.XPATH,"//button[@id='but2']").is_enabled():
    print("Button 2 is enabled")
else:
    print("Button 2 is disabled")

if driver.find_element(By.XPATH,"//button[@id='but1']").is_enabled():
    print("Button 1 is enabled")
else:
    print("Button 1 is disabled")

time.sleep(2)
driver.quit()

