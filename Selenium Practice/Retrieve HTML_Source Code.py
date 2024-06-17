import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://omayo.blogspot.com/")
# driver.fullscreen_window() # To Open in Full screen window
# driver.set_window_size(800,300)
time.sleep(2)
driver.refresh()
driver.maximize_window()

Code = driver.page_source
print(Code)