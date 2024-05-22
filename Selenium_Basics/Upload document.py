from Setup_Files import Setup as stp

stp.driver.get("https://cgi-lib.berkeley.edu/ex/perl5/fup.html")
stp.driver.find_element(stp.By.XPATH,"//input[@name='upfile']").send_keys("C:\\Users\\Madhu Kumar PSI-3442\\Desktop\\Selenium\\file-sample_100kB.docx")
stp.time.sleep(5)
