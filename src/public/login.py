#coding=utf-8
from selenium import webdriver
import BaseFunction
from config import constants
import os
class Login:
    def __init__(self):
        os.environ["webdriver.firefox.bin"] = constants.firefoxBin
        self.driver=webdriver.Firefox()
        self.url = constants.web_url
        
    def login(self,driver,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
        BaseFunction.getLocator(self.driver, "input1").send_keys(constants.username)
        BaseFunction.getLocator(self.driver, "pwd_input").send_keys(constants.password)
        BaseFunction.getLocator(self.driver, "login_button").click()
    def getDriver(self):
        return self.driver
    
    def getUrl(self):
        return self.url
    
if __name__=="__main__":
    pass
        
        