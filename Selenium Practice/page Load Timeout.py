import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.set_page_load_timeout(7)
driver.get("https://omayo.blogspot.com/")
time.sleep(2)
driver.refresh()
driver.maximize_window()
time.sleep(2)
driver.quit()