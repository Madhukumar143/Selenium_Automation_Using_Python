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
        driver.get("https://www.snapdeal.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//input[@id='inputValEnter']").send_keys("mobile phones")
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[contains(@class,'searchformButton')]").click()
        time.sleep(3)
        Start_element = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
        End_element = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
        act = ActionChains(driver)
        #act.click_and_hold(Start_element).pause(1).move_by_offset(50,0).release().perform()
        #act.drag_and_drop_by_offset(Start_element, 10, 0).perform()
        act.move_to_element(Start_element).pause(1).click_and_hold(Start_element).move_by_offset(80,0).release().perform()
        act.move_to_element(End_element).pause(1).click_and_hold(End_element).move_by_offset(-20,0).release().perform()
        time.sleep(3)

        time.sleep(3)

        achains = ActionChains(driver)


Mouse_object = Mouse_Over()
Mouse_object.Mouse()