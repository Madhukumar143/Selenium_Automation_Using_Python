import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://omayo.blogspot.com/")
time.sleep(2)

links = driver.find_elements(By.XPATH,"//a")
print(len(links))

for i in links:
    print(i.get_attribute("href"))

time.sleep(2)
