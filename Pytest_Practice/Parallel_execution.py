import time
# use this command pytest parallel_execution.py -n 3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_omayo_blogspot():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/#")
    time.sleep(2)
    driver.quit()

def test_Selenium_Blogspot():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium143.blogspot.com/")
    time.sleep(2)
    driver.quit()

def test_jquery():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/")
    time.sleep(2)
    driver.quit()