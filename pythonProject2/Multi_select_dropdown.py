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

class MultiSelect_Dropdown():
    def Multiselect(self):
        driver.get("https://demoqa.com/select-menu")
        # Maximize the window opened
        driver.maximize_window()
        cars = Select(driver.find_element(By.XPATH," //select[@id='cars']"))
        cars.select_by_index(1)
        cars.select_by_visible_text("Audi")
        time.sleep(2)

Mustiselect_object = MultiSelect_Dropdown()
Mustiselect_object.Multiselect()