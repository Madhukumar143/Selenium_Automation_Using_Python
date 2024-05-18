import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

datetime = datetime.now()
print(datetime)

Date = "15"
ch_option =Options()
ch_option.add_experimental_option('detach', True)
ser_obj = Service("D:\\Automation\\Selenium\\Python_Project_SDET\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj, options=ch_option)

driver.get("https://dummyticket.com/dummy-ticket-for-visa-application/")

# Maximize the window opened
driver.maximize_window()

