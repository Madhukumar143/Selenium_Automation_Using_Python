import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Month_dictionary = {"January" : 1,"February" : 2, "March":3,"April":4, "May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
datetime = datetime.now()
print(datetime)

Date = "15"
ch_option =Options()
ch_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(ch_option)

driver.get("https://dummyticket.com/dummy-ticket-for-visa-application/")

# Maximize the window opened
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click()
Select_Month = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
Select_Month.select_by_visible_text("Apr")

Select_Year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
Select_Year.select_by_visible_text("1998")

#NoOfRows = len(driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr"))
#NoOfCols = len(driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr["+str(1)+"]/td"))

all_dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for date in all_dates:
    if date.text == "24":
        date.click()
        break

'''for i in range (1,6):
    for j in range(1,8):
        Date_table = driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr["+str(i)+"]/td["+str(j)+"]")
        Compare_Date = Date_table.text
        if Compare_Date == Date:
            Date_table.click()
            print("date of birth is selected")'''

time.sleep(5)