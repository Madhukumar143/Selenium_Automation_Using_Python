import time
from datetime import date, datetime

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window
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
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# Scroll Down Page by Pixel
#driver.execute_script(("window.scrollBy(0,4000)"),"")
#value = driver.execute_script("return window.pageYOffset;")
#print(value)

# scroll down till the element is visible
#value = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
#driver.execute_script("arguments[0].scrollIntoView();",value)
#Offset = driver.execute_script("return window.pageYOffset;")
#print(Offset)

#Scroll Down till the page end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
Offset = driver.execute_script("return window.pageYOffset;")
print(Offset)
time.sleep(3)

# Scroll to Initial point (start)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
Offset = driver.execute_script("return window.pageYOffset;")
print(Offset)
time.sleep(5)

