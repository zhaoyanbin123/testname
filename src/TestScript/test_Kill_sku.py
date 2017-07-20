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

    def test_Kill_sku(self):
        self.driver.implicitly_wait(30)
        
        BaseFunction.getLocator(self.driver, "page_button").click()


if __name__ == "__main__":
    unittest.main()