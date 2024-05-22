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
'''ch_option =Options()
driver = webdriver.Chrome(ch_option)'''
ser_obj = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
class Demo_Multiple_windows():
    def Multiple_windows(self):
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH,"//img[@class='conta iner']").click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle!= parent_handle:
                driver.switch_to.window(handle)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(2)
                driver.find_element(By.XPATH,"//a[normalize-space()='Terms and Conditions']").click()
                time.sleep(1)
        handles = driver.window_handles
        for i in handles:
            driver.switch_to.window(i)
            time.sleep(1)
            #print(driver.title)
            if driver.title != "Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com":
                driver.close()
                time.sleep(1)
            else:
                continue
        #driver.switch_to.window(parent_handle)
        #driver.find_element(By.XPATH, "//img[@class='conta iner']").click()
        time.sleep(4)

Multi_window_object = Demo_Multiple_windows()
Multi_window_object.Multiple_windows()
