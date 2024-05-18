import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import Valid_login as val
val.Login()
val.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]").click()
time.sleep(3)
val.driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
val.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div").click()
time.sleep(4)