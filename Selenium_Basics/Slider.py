import time
from datetime import date, datetime

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#to print the time of test run
datetime = datetime.now()
print(datetime)
# # Enter the User-name and password Manually
# EmailId = "teacher@giis.com"#input("enter the email id")
# password = "Test@1234"#input("enter the password")
ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
time.sleep(5)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

act =ActionChains(driver)
#slider
min_slider = driver.find_element(By.XPATH,"//span[1]")
max_slider = driver.find_element(By.XPATH,"//span[2]")

print(min_slider.location) #{'x': 59, 'y': 250}
print(max_slider.location) #{'x': 510, 'y': 250}

act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-35,0).perform()

print(min_slider.location) #{'x': 158, 'y': 250}
print(max_slider.location) #{'x': 474, 'y': 250}






