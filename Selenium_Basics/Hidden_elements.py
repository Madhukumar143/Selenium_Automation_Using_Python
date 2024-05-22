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
class DemoHiddenElements():
    def demo_is_Displayed(self):
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        # Maximize the window opened
        driver.maximize_window()
        elem = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem)
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        elem = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem)

    def demo_is_displayed_yatra(self):
        driver.get("https://www.yatra.com/hotels")
        # Maximize the window opened
        driver.maximize_window()
        driver.find_element(By.XPATH, "//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(2)
        for i in range(3):
            driver.find_element(By.XPATH, "(//span[@class='ddSpinnerPlus'])["+str(2)+"]").click()
        elem = driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(elem)
        time.sleep(3)
        #driver.find_element(By.XPATH, "(//span[@class='ddSpinnerMinus'])[2]").click()
        #time.sleep(5)
        child_count_below_12_years = int(driver.find_element(By.XPATH, "//span[@class='pax-num-child adultcount']").text)
        print(child_count_below_12_years)
        # if the children below 12 years is zero then selecting age element is not present in DOM.
        # handling this using exceptions
        try:
            # identify element
            elem = driver.find_element(By.XPATH,"//select[@class='ageselect']")
            print("Element exist to select the age of the children")
        # NoSuchElementException thrown if not present
        except NoSuchElementException:
           print("Element does not exist because children count below 12 years is 0")

        if (child_count_below_12_years > 0):
            for i in range (1,int(child_count_below_12_years)+1):
                select_age = Select(driver.find_element(By.XPATH,"(//li[@class='childageselect'])["+str(i)+"]//select"))
                select_age.select_by_visible_text('10')





demoDisplayed = DemoHiddenElements()
#demoDisplayed.demo_is_Displayed()
demoDisplayed.demo_is_displayed_yatra()