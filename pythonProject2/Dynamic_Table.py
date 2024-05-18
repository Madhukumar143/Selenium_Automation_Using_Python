import time
from datetime import date, datetime
from selenium.webdriver.chrome.options import Options
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
No_Of_Rows = len(driver.find_elements(By.XPATH,"//table[@id='productTable']/tbody/tr"))
driver.find_element(By.XPATH,"//table[@id='productTable']/tbody/tr["+str(3)+"]/td["+str(4)+"]/input[@type='checkbox']").click()
print(No_Of_Rows)
time.sleep(5)

for i in range(No_Of_Rows):
    Checkbox_data = driver.find_element(By.XPATH,"//table[@id='productTable']/tbody/tr["+str(i+1)+"]/td["+str(4)+"]/input[@type='checkbox']").is_selected()
    print(Checkbox_data)


