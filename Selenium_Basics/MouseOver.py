import time
from datetime import date, datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

datetime = datetime.now()
print(datetime)
ch_option =Options()
driver = webdriver.Chrome(ch_option)

class Mouse_Over():
    def Mouse(self):
        driver.get("https://www.yatra.com/hotels")
        driver.maximize_window()
        over_ele = driver.find_element(By.XPATH,"//span[@class='more-arr']")
        My_Account = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
        achains = ActionChains(driver)
        achains.move_to_element(My_Account).perform()
        time.sleep(3)
        achains.move_to_element(over_ele).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(5)

Mouse_object = Mouse_Over()
Mouse_object.Mouse()