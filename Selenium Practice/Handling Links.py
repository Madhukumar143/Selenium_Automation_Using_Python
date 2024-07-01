import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.implicitly_wait(5)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
for i in range(1,6):
    xpath = "(//div[@id='LinkList1']//a)["+str(i)+"]"
    link = driver.find_element(By.XPATH,xpath)
    link.click()
    if driver.title is None:
        print("404 not found")
    print(driver.title)
    driver.back()

time.sleep(5)