import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
#information pop up with only one ok option

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
alrt = driver.switch_to.alert
time.sleep(1)
print(alrt.text)
alrt.accept()
time.sleep(1)
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(3)
Alert_2 = driver.switch_to.alert
Alert_2.dismiss() # to dismiss
#Alert_2.accept()
#if no alert is present and if user switched to alert it will through no alert exception
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Elemental Selenium").click()
driver.switch_to.window(driver.title)
driver.close()
time.sleep(3)

