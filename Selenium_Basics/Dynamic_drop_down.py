from selenium.webdriver.common.by import By
from Setup_Files import Setup as stp

stp.driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
stp.driver.maximize_window()
stp.driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countrys = stp.driver.find_elements(By.XPATH,"//span[@class='select2-results']/ul/li")

for country_name in countrys :
    if country_name.text == "Albania":
        country_name.click()
        break
stp.time.sleep(3)
