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

driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
driver.maximize_window()#driver.add_argumrnt("--start-maximized")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("Madhu")

Web_Page_Height = driver.execute_script("return Math.max(document.body.scrollHeight,document.body.offsetHeight,document.documentElement.clientHeight,document.documentElement.scrollHeight,document.documentElement.offsetHeight)")
print(Web_Page_Height)
AC = ActionChains(driver)

AC.send_keys(Keys.TAB).pause(2).send_keys("Kumar").send_keys(Keys.TAB).pause(2)\
  .send_keys("madhukumarhm123.com@gmail.com").send_keys(Keys.TAB).pause(2).send_keys("8296790418").perform()

time.sleep(5)