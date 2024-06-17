import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

if driver.find_element(By.XPATH,"//input[@id='radio1']").is_selected():
    print("Selected State radio button")
else:
    print("Unselected State radio button")

if driver.find_element(By.XPATH,"//input[@id='checkbox1']").is_selected():
    print("Selected State Check Box")
else:
    print("Unselected State Check Box")

time.sleep(3)
driver.quit()

