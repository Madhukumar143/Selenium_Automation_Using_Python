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
driver.implicitly_wait(10)

'''class Demo_Frames():
    def demo_iframes(self):
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.switch_to.frame('iframeResult')
        driver.switch_to.frame(0)
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[@id='navbtn_exercises']").click()
        time.sleep(2)

diframe = Demo_Frames()
diframe.demo_iframes()'''

'''driver.get("https://docs.oracle.com/javase/8/docs/api/")
driver.switch_to.frame("classFrame")
driver.find_element(By.LINK_TEXT,"Description").click()'''
driver.get("https://blogpendingtasks.blogspot.com/p/switchtoframeusingwebelement.html")
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='arunmotoori']"))
driver.find_element(By.LINK_TEXT,"Home").click()
time.sleep(3)