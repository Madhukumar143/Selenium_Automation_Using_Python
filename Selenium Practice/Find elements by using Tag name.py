import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://omayo.blogspot.com/")

links = driver.find_elements(By.TAG_NAME,"a")
for link in links:
     print(link.get_attribute("href"))

time.sleep(3)
