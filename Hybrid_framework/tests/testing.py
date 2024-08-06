from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php")
driver.find_element(By.XPATH,"//span[contains(text(),'My Account')]").click()
driver.find_element(By.LINK_TEXT,"Login").click()
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("madhukumarhm605@gmail.com")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Madhu@1234")
driver.find_element(By.XPATH,"//input[@type='submit']").click()