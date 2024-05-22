import time
from datetime import date, datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

datetime = datetime.now()
print(datetime)
ch_option =Options()
driver = webdriver.Chrome(ch_option)

class Wait():
    def implicit_wait(self):
        driver.get("https://login.salesforce.com/?locale=in")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Madhu virat")
        driver.find_element(By.XPATH, "//input[@id='passwod']").send_keys("madhu@1234")

    def Explicit_wait(self):
        driver.get("https://www.yatra.com/")
        # Maximize the window opened
        driver.maximize_window()
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver,10)

        Origin_City = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        Origin_City.clear()
        #wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']"))).click()
        #driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").click()
        Origin_City.send_keys("Mumbai")
        wait.until(EC.presence_of_element_located((By.XPATH, "(//p[@class='ac_cityname'])[2]")))
        Origin_City.send_keys(Keys.ENTER)
        time.sleep(3)


        '''Arrival_City = driver.find_element(By.XPATH, "//input[@id ='BE_flight_arrival_city']")
        #Arrival_City.clear()
        Arrival_City.send_keys("Mu")
        Search_Results = driver.find_elements(By.XPATH, "(//div[@class='viewport'])//li")
        for results in Search_Results:
            if "Mumbai (BOM)" in results.text:
                results.click()
                break
        time.sleep(5)
        all_dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//table//tbody//td[@class!='inActiveTD weekend']")
        for date in all_dates:
            if date.get_attribute("id") == "20/06/2024":
                date.click()
                time.sleep(3)
                break
        time.sleep(5)'''




Mouse_object = Wait()
Mouse_object.Explicit_wait()