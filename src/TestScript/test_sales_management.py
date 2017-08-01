#coding=utf-8
import unittest
from public import BaseFunction,login

class Test(unittest.TestCase):


    def setUp(self):
        self.dr=login.Login()
        self.driver=self.dr.getDriver()
        self.url=self.dr.getUrl()
        self.dr.login(self.dr.getDriver(),self.url)


    def tearDown(self):
        self.driver.quit()
        


    def test_asles_management(self):
        
        self.driver.implicitly_wait(30)
        #销售管理
        BaseFunction.getLocator(self.driver, "sales_button").click()
        


if __name__ == "__main__":
    unittest.main()