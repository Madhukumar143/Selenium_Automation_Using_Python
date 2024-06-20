import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ch_options = Options()
driver=webdriver.Chrome(options=ch_options)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Admin']").click()

driver.find_element(By.XPATH,"(//i[@class='oxd-icon bi-trash'])[2]").click()
#driver.find_element(By.XPATH,"//button[normalize-space()='×']").click()
a = driver.find_element(By.XPATH,"//div[@role='document']")
print(a)
time.sleep(3)

