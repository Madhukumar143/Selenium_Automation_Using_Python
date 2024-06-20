import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
ch_options.add_argument("--disable_notifications")
driver=webdriver.Chrome(options=ch_options)
driver.get("https://www.homedepot.com/")
driver.maximize_window()
time.sleep(10)
