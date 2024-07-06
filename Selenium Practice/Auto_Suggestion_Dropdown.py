import time
from datetime import date, datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

datetime = datetime.now()
print(datetime)
ch_option =Options()
ch_option.add_experimental_option("excludeSwitches",["enable-automation"])
#ch_option.add_experimental_option("useAutomationExtension",False)
#ch_option.add_argument("--disable-blink-features=automationControlled")
driver = webdriver.Chrome(ch_option)
driver.implicitly_wait(3)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//label[@for='fromCity']").click()
driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("mad")
time.sleep(8)
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
            time.sleep(5)
            print(Airport_name+" Airport is Selected for From Destination")
            exit()

    else:
        xpath = "(//ul//li//div//div//div//div//p)["+str(i-len(expect))+"]"
        Airport = driver.find_element(By.XPATH, xpath)
        Airport_name = Airport.text
        print(Airport_name)
        if Airport_name == "Madeira, Portugal":
            Airport.click()
            time.sleep(5)
            print(Airport_name + " Airport is Selected for From Destination")
            exit()
