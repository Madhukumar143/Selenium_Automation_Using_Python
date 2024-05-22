from selenium.webdriver.common.by import By

from Setup_Files import Setup as stp

'''stp.driver.get("https://testautomationpractice.blogspot.com/")
stp.driver.switch_to.new_window("tab")
stp.driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

stp.driver.get("https://testautomationpractice.blogspot.com/")
stp.driver.switch_to.new_window("window")
stp.driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")'''
stp.driver.get("https://demo.nopcommerce.com/")
stp.driver.maximize_window()
reglink = stp.Keys.CONTROL+stp.Keys.RETURN
stp.driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)
stp.time.sleep(5)