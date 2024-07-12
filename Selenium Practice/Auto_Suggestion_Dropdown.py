import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

datetime = datetime.now()
print(datetime)
ch_option =Options()
ch_option.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(ch_option)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.makemytrip.com/")

driver.find_element(By.XPATH,"//label[@for='fromCity']").click()
driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("mad")
#time.sleep(8)
expect = driver.find_elements(By.XPATH,"//ul[contains(@role,'listbox')]//li//div//div//p//span//span")
actual = driver.find_elements(By.XPATH,"//ul//li//div//div//div//div//p")
#a = driver.find_element(By.XPATH,"(//ul[contains(@role,'listbox')]//li//div//div//p//span//span)[1]").text
#print(a)
length = len(actual)+len(expect)
"""for i in range(1,len(expect)+1):
    xpath = "(//ul[contains(@role,'listbox')]//li//div//div//p//span//span)["+str(i)+"]"
    print(driver.find_element(By.XPATH,xpath).text)"""
for i in range(1,length+1):
    if i <= len(expect):
        xpath = "(//ul[contains(@role,'listbox')]//li//div//div//p//span//span)[" + str(i) + "]"
        Airport = driver.find_element(By.XPATH, xpath)
        Airport_name = Airport.text
        print(Airport_name)
        if Airport_name == "Madeira, Portugal":
            Airport.click()
            print(Airport_name+" Airport is Selected for From Destination")
            exit()

    else:
        xpath = "(//ul//li//div//div//div//div//p)["+str(i-len(expect))+"]"
        Airport = driver.find_element(By.XPATH, xpath)
        Airport_name = Airport.text
        print(Airport_name)
        if Airport_name == "Madeira, Portugal":
            Airport.click()
            print(Airport_name + " Airport is Selected for From Destination")
            exit()
