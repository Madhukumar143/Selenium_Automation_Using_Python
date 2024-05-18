import time
from datetime import date, datetime
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# print the present date and time
datetime = datetime.now()
print(datetime)
Ch_Options = Options()

#ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(Ch_Options)

Ch_Options.add_argument("--incognito")
# to stop the browser automatically stopping the application
driver.get("https://terralogic.paxanimi.ai/login")
# Maximize the window opened

driver.maximize_window()
driver.find_element(By.XPATH,"//div[contains(text(),'Terralogic Login')]").click()
time.sleep(40)