import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
ch_options = Options()
driver=webdriver.Chrome(ch_options)
driver.implicitly_wait(5)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
'''Drop = driver.find_element(By.XPATH,"//select[@id='drop1']")
select = Select(Drop)
#select.select_by_visible_text("doc 1")
#select.select_by_index(4)
select.select_by_value("ghi")'''
Multi_Select = driver.find_element(By.XPATH,"//select[@id='multiselect1']")
Multi = Select(Multi_Select)
Multi.select_by_index(3)
Multi.select_by_visible_text("Swift")
Multi.select_by_value("volvox")
Multi.select_by_index(0)
time.sleep(3)
print(Multi.first_selected_option.text)
Mul_Options = Multi.all_selected_options
 
for i in Mul_Options:
    print(i.text)

Multi.deselect_all()
'''Multi.deselect_by_index(3)
Multi.deselect_by_value("volvox")
Multi.deselect_by_visible_text("Swift")'''

drop = Multi.options
for i in drop:
    print(i.text)
time.sleep(3)
