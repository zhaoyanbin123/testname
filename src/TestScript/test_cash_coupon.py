#coding=utf-8
import unittest
from public import BaseFunction,login
import time
from selenium.webdriver.support.select import Select

class Test(unittest.TestCase):

    def setUp(self):
        self.coupon_price=raw_input("请输入现金券金额:")
        self.phone=raw_input("请输入下发手机号：")
        self.dr=login.Login()
        self.driver=self.dr.getDriver()
        self.url=self.dr.getUrl()
        self.dr.login(self.dr.getDriver(),self.url)

    def tearDown(self):
        pass
        self.driver.quit()

    def test_cash_coupon(self):
        
        self.driver.implicitly_wait(30)
        BaseFunction.getLocator(self.driver, "coupon_button").click()
        BaseFunction.getLocator(self.driver, "coupon_button_1").click()
        BaseFunction.getLocator(self.driver, "coupon_add_button").click()
        
        select = Select(BaseFunction.getLocator(self.driver,"coupon_type_select_1"))
        select.select_by_value("2")
        
        BaseFunction.getLocator(self.driver,"coupon_type_button").click()
        BaseFunction.getLocator(self.driver,"coupon_name_text").send_keys(u"测试现金券")
        BaseFunction.getLocator(self.driver,"coupon_value_text").send_keys(self.coupon_price)
        
        BaseFunction.getLocator(self.driver,"coupon_time_type").click()
        BaseFunction.getLocator(self.driver, "expired_after_text").send_keys(2)
        
        BaseFunction.getLocator(self.driver,"coupon_total_text").click()
        BaseFunction.getLocator(self.driver,"coupon_total_text").send_keys(1)
        
        BaseFunction.getLocator(self.driver,"save_button").click()
        self.driver.switch_to_alert().accept()
        
        time.sleep(3)
        
        now_handle = self.driver.current_window_handle #获取当前窗口句柄
        BaseFunction.getLocator(self.driver,"view_button").click()
        time.sleep(3)
        all_handles = self.driver.window_handles #获取所有窗口句柄
        
        for handle in all_handles:
            if handle!=now_handle:
                self.driver.switch_to_window(handle)
                js="var q=document.documentElement.scrollTop=5000"
                self.driver.execute_script(js)
                BaseFunction.getLocator(self.driver, "Nodown_button").click()
                BaseFunction.getLocator(self.driver,"down_button").click()
                BaseFunction.getLocator(self.driver,"phone_text").send_keys(self.phone)
                BaseFunction.getLocator(self.driver,"query_button").click()
                BaseFunction.getLocator(self.driver,"query_button_1").click()
                break
            

if __name__ == "__main__":
    unittest.main()