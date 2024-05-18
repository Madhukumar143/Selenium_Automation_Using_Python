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

class DemoJS():
    def demo_JavaScript(self):
        driver.execute_script("window.open('https://training.rcvacademy.com/','_self')")
        time.sleep(6)
        demo_element =driver.execute_script("return document.getElementsByTagName('a')[10];")
        driver.execute_script("arguments[0].click();",demo_element)
        time.sleep(2)
Js_Object = DemoJS()
Js_Object.demo_JavaScript()