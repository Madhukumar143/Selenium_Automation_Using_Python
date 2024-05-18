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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
Hover = driver.find_element(By.XPATH,"//a[normalize-space()='open cart']")

act =ActionChains(driver)
# Mouse hover
#act.move_to_element(Hover).click().perform()

# Right click
#driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='frame-one796456169']"))
#Right_Click = driver.find_element(By.XPATH,"//input[@type='submit']")
#act.context_click(Right_Click).perform()
#driver.switch_to.frame(id="frame-one796456169")

# Double Click
driver.find_element(By.XPATH,"//input[@id='field1']").clear()
driver.find_element(By.XPATH,"//input[@id='field1']").send_keys("Madhu Virat")
doubleClick= driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act.double_click(doubleClick).perform()

# Drag and Drop
Source_ele= driver.find_element(By.XPATH,"//div[@id='draggable']")
Target_ele= driver.find_element(By.XPATH,"//div[@id='droppable']")
act.drag_and_drop(Source_ele,Target_ele).perform()

#slider
Start_element = driver.find_element(By.XPATH,"//span[@style='left: 0%;']")

act.drag_and_drop_by_offset(Start_element,200,0).perform()

time.sleep(5)

