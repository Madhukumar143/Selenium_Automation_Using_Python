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

driver.get("https://jqueryui.com/resizable/")
driver.maximize_window()
time.sleep(3)

driver.switch_to.frame(0)
AC = ActionChains(driver)
Element = driver.find_element(By.CSS_SELECTOR,"div.ui-icon-gripsmall-diagonal-se")
AC.drag_and_drop_by_offset(Element,15,20).perform()
time.sleep(4)
