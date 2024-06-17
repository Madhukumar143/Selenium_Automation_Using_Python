import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

if driver.find_element(By.XPATH,"//input[@id='hbutton']").is_displayed():
    print("element is displayed")
else:
    print("element is not displayed")

time.sleep(3)
driver.quit()