import time
from datetime import date, datetime
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
location = "C:\\Users\\Madhu Kumar PSI-3442\\Desktop\\Selenium"
preferances = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
ops = webdriver.ChromeOptions()
ops.add_experimental_option("prefs",preferances)
from selenium.webdriver.common.by import By
#to print the time of test run
datetime = datetime.now()
print(datetime)
ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj,options=ops)
time.sleep(3)


#import Setup as stp
#Explicitly for PDF
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
#driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(10)
