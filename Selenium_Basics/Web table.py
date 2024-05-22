import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

datetime = datetime.now()
print(datetime)

ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)

driver.get('https://testautomationpractice.blogspot.com/')

# Maximize the window opened
driver.maximize_window()
time.sleep(2)

# Find the Number of Rows and coloumns
NoOfRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
NoOfCols = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr//th"))

print("No of rows = ",NoOfRows,"\n" "No of columns = ", NoOfCols)

# read Specific Row or Column data
a = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print()
print(a,"\n")

# Read all the rows and columns data
for row in range(2,NoOfRows+1):
    for col in range(1,NoOfCols+1):
        m = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
        print(m,end="    ")
    print("\n")

#print book name by author name as mukesh

for r in range(2,NoOfRows+1):
    author_name= driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        Subject = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[3]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print("book name = ", book_name)
        print("Subject = ", Subject)
        print("price = ",price)
    print()
