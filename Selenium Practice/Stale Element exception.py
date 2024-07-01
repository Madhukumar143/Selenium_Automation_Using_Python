import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.implicitly_wait(5)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

text_field = driver.find_element(By.XPATH,"//textarea[@id='ta1']")
text_field.send_keys("Madhu Virat")

time.sleep(2)
driver.find_element(By.LINK_TEXT,"compendiumdev").click()
time.sleep(2)
driver.back()
'''after going from the page and revisited again assigned Xpaths should be reassingned 
or else it will through stale element reference exception'''

time.sleep(2)
text_field = driver.find_element(By.XPATH,"//textarea[@id='ta1']")
text_field.clear()
time.sleep(3)
