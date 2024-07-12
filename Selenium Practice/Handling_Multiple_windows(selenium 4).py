import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

datetime = datetime.now()
print(datetime)
ch_option =Options()
ch_option.add_experimental_option("excludeSwitches",["enable-automation"])
#ch_option.add_experimental_option("useAutomationExtension",False)
#ch_option.add_argument("--disable-blink-features=automationControlled")
driver = webdriver.Chrome(ch_option)
driver.implicitly_wait(3)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()#driver.add_argumrnt("--start-maximized")
print(driver.title)
time.sleep(4)
driver.switch_to.new_window("tab")
time.sleep(3)
driver.get("https://selenium143.blogspot.com/")
time.sleep(3)
print(driver.title)




"""parent_window_id = driver.current_window_handle
driver.find_element(By.LINK_TEXT,"Open a popup window").click()
windows = driver.window_handles#stores ids of all the windows opened

for window in windows :
    driver.switch_to.window(window)
    if driver.title == "New Window":
        a = driver.find_element(By.XPATH,"//div[@class='example']//h3").text
        print(a)
        break

driver.switch_to.window(parent_window_id)
print(driver.find_element(By.XPATH,"//h3[@class='post-title entry-title']").text)
time.sleep(2)"""