import time
from datetime import date, datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

datetime = datetime.now()
print(datetime)
ch_option =Options()
driver = webdriver.Chrome(ch_option)

class Demo_Alerts():
    def Alerts(self):
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        time.sleep(3)
        driver.switch_to.frame("iframeResult")
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(2)
        #dismiss Alert
        #driver.switch_to.alert.dismiss()
        #time.sleep(2)
        print(driver.switch_to.alert.text)

        #Send text in alert
        driver.switch_to.alert.send_keys("Iron Man")
        time.sleep(2)

        # Accept Alert
        driver.switch_to.alert.accept()
        time.sleep(2)


Alerts_object = Demo_Alerts()
Alerts_object.Alerts()