import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='justAnInputBox']").click()
driver.find_element(By.XPATH,"(//span[contains(text(),'choice 4')])[1]").click()
driver.find_element(By.XPATH,"(//span[contains(text(),'choice 6')])[1]").click()
driver.find_element(By.XPATH,"(//span[contains(text(),'choice 6 2 2')])[1]").click()
driver.find_element(By.XPATH,"//div[@id='jquery-script-menu']/following-sibling::div/h1").click()

time.sleep(3)
