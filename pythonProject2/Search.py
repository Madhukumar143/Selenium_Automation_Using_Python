import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import Valid_login as val
val.Login()
#val.driver.find_element(By.XPATH,"//input[@placeholder='Search']").click()
val.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
val.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div").click()
drop.select_by_visible_text("Deeksha Collings")
time.sleep(3)
