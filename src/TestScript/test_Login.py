# coding=utf-8
import unittest
from public import BaseFunction,login

class Test(unittest.TestCase):


    def setUp(self):
        self.dr=login.Login()
        self.driver=self.dr.getDriver()
        self.url=self.dr.getUrl()

    def tearDown(self):
        self.driver.quit()


    def test_login(self):
        
        self.dr.login(self.dr.getDriver(),self.url)
        
        self.driver.implicitly_wait(30)
        
        print "校验是否登录成功"
        '''判断是否存在已编辑按钮'''
         
        if BaseFunction.getLocator(self.driver, "page_button").is_enabled():
            print "登录成功"
        else:
            print "登录失败"
            
        
        
if __name__ == "__main__":
    unittest.main()
