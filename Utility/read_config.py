from configparser import ConfigParser

def get_config(category, key):
    con = ConfigParser()
    con.read("C:\\Pytest_DemoWebShop1\\Configurations\\config.ini")
    return con.get(category, key)
