from Setup_Files import Setup as stp

stp.driver.get("https://demo.nopcommerce.com/")
stp.driver.maximize_window()

#capture cookies from browser
cookies = stp.driver.get_cookies()
print("Size of cookies initially",len(cookies))

stp.driver.add_cookie({"name":"Mycookies","value":"123456"})
cookies1 = stp.driver.get_cookies()
print("Size of cookies after adding",len(cookies1))

stp.driver.delete_cookie("Mycookies")
cookies2= stp.driver.get_cookies()
print("Size of cookies after deleting",len(cookies2))

for c in cookies2:
    #print(c)
    print(c.get("name"),":",c.get("value"),":",c.get("expiry"))

'''stp.driver.add_cookie({"name":"Mycookies","value":"123456"})
cookies = stp.driver.get_cookies()
print("Size of cookies after adding",len(cookies))'''

'''stp.driver.delete_cookie("Mycookies")
cookies = stp.driver.get_cookies()
print("Size of cookies after deleting",len(cookies))'''

stp.time.sleep(3)