import time
from datetime import date, datetime
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#to print the time of test run
datetime = datetime.now()
print(datetime)
ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
time.sleep(5)
driver.get("https://text-compare.com/")
driver.maximize_window()
first_box = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
second_box = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
first_box.clear()
second_box.clear()

driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("EE SALA CUP NAMDE")
#first_box.click
act = ActionChains(driver)
#key_down -> click the key key_up -> release the key
# ctrl+a
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#ctrl+c
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
driver.find_element(By.XPATH,"//textarea[@id='inputText2']").clear()

# go to second box or (tab key-> act.send_keys(Keys.TAB).perform())
second_box.click()

#ctrl+v
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)

if first_box.text == second_box.text:
    print("text in both the containers is matched")
else:
    print("text in both the containers is not matched")