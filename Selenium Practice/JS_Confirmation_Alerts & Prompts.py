import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
#information pop up with only one ok option
time.sleep(1)
#Confirmation pop up
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(3)
Conf_alert = driver.switch_to.alert
Conf_alert.dismiss()
time.sleep(3)
# JS Prompt
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
prompt = driver.switch_to.alert
prompt.send_keys("EE Sala Cup Namde")
prompt.accept()
time.sleep(2)
