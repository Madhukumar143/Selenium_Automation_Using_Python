import time
from datetime import date, datetime
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
location = "C:\\Users\\Madhu Kumar PSI-3442\\Desktop\\Selenium"
preferances = {"download.default_directory":location,"plugins.alwyas_open_pdf_externally":True}
ops = webdriver.ChromeOptions()
ops.add_experimental_option("prefs",preferances)
from selenium.webdriver.common.by import By
#to print the time of test run
datetime = datetime.now()
print(datetime)
ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
time.sleep(3)