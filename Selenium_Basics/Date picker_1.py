import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
Month_dictionary = {"January" : 1,"February" : 2, "March":3,"April":4, "May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
datetime = datetime.now()
print(datetime)

ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)

driver.get("https://jqueryui.com/datepicker/")

# Maximize the window opened
driver.maximize_window()
Actual_month = "March"
Actual_year = "2022"
Actual_date = "3"
driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("01/08/2024")
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

#date_1 = driver.find_element(By.XPATH,"//input[@id='datepicker']")
'''date_1.send_keys("04/20/2012")
date_1.send_keys(Keys.ENTER)
time.sleep(3)

'''
time.sleep(2)
initial_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
initial_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

# selecting required year and month
while True:
    Month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if initial_year > Actual_year :
        if (year != Actual_year):
            driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
        else:
            if Month != Actual_month:
                driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
            else:
                break
    elif initial_year < Actual_year :
        if (year != Actual_year):
            driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        else:
            if Month != Actual_month :
                driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
            else :
                break
    else:
        if Month_dictionary[initial_month] > Month_dictionary[Actual_month] :
            if Month != Actual_month:
                driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
            else:
                break
        elif Month_dictionary[initial_month] < Month_dictionary[Actual_month] :
            if Month != Actual_month:
                driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
            else:
                break
        else:
            break

for i in range (1,6):
    for j in range(1,8):
        Date = driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr["+str(i)+"]/td["+str(j)+"]")
        Compare_Date = Date.text
        if Compare_Date == Actual_date :
            Date.click()
time.sleep(8)