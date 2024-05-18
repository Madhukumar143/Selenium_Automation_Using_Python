import os
from Setup_Files import Setup as stp

stp.driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
stp.driver.maximize_window()
#stp.driver.save_screenshot("C:\\Users\\Madhu Kumar PSI-3442\\Desktop\\Selenium\\Screenshot.png")
#stp.driver.save_screenshot(os.getcwd()+"\\Home.png")
stp.driver.get_screenshot_as_file(os.getcwd()+"\\Screenshot_as file.png")
#stp.driver.get_screenshot_as_png("C:\\Users\\Madhu Kumar PSI-3442\\Desktop\\Selenium\\Screenshot_as_png.png")