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

driver.get("https://omayo.blogspot.com/#")
driver.maximize_window()
time.sleep(3)
action_chains = ActionChains(driver)
links = driver.find_elements(By.XPATH,"(//div[@id='LinkList1']//div[@class='widget-content']//a)")

for link in links:
    action_chains.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    time.sleep(1)

time.sleep(6)
#driver.quit()