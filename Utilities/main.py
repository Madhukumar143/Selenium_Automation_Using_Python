from configparser import ConfigParser


def get_config(category,key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(category,key)

login_URL = get_config("basic info","Url")
Login_Browser = get_config("basic info","Browser")

User_name_Xpath = get_config("Locators for login","Usr_Name")
User_Password_Xpath = get_config("Locators for login","Usr_Pswrd")

print(login_URL,Login_Browser,User_name_Xpath,User_Password_Xpath)

