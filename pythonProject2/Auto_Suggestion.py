import time
from datetime import date, datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

datetime = datetime.now()
print(datetime)
ch_option =Options()
driver = webdriver.Chrome(ch_option)

class Demo_Auto_Suggest():
    def Auto_Suggest(self):
        driver.get("https://www.yatra.com/")
        # Maximize the window opened
        driver.maximize_window()
        Origin_City = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        Origin_City.click()
        time.sleep(2)
        Origin_City.clear()
        Origin_City.send_keys("Ba")
        time.sleep(3)
        Origin_City.send_keys(Keys.ENTER)
        time.sleep(2)
        Arrival_City = driver.find_element(By.XPATH, "//input[@id ='BE_flight_arrival_city']")
        Arrival_City.clear()
        Arrival_City.send_keys("Mu")
        Search_Results = driver.find_elements(By.XPATH,"(//div[@class='viewport'])//li")
        print([i.text for i in Search_Results])
        print(len(Search_Results))

        for results in Search_Results:
            if "Mumbai (BOM)" in results.text:
                results.click()
                break

        time.sleep(5)

    def Select_dates(self):
        driver.get("https://www.yatra.com/")
        # Maximize the window opened
        driver.maximize_window()
        driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()
        time.sleep(3)
        '''b=input("Enter the date in the format (dd/mm/yyyy)")
        a="@id="+"'"+b+"'"
        time.sleep(2)
        print(a)
        driver.find_element(By.XPATH,'//td['+a+']').click()
        time.sleep(3)'''
        all_dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//table//tbody//td[@class!='inActiveTD weekend']")
        for date in all_dates:
            if date.get_attribute("id") == "20/06/2024":
                date.click()
                time.sleep(3)
                break
            #print(all_dates)



Auto_suggest_object = Demo_Auto_Suggest()
#suggest_object.Auto_Suggest()
Auto_suggest_object.Select_dates()