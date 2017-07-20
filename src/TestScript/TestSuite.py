#coding=utf-8
import unittest
from TestScript import test_all_skulist
from TestScript import test_Login
import os,sys
reload(sys)
'''获取所有的测试case加载到测试套件中'''
def TestSuite():
    '''不要放在class内,否则会提示"没有这样的测试方法在<class'myapp.tests.SessionTestCase'>：的runTest "'''
    suite=unittest.TestSuite()
    suite.addTest(test_all_skulist.Test("test_all_skulist"))
    suite.addTest(test_Login.Test("login_test"))
    return suite


'''在testdir目录下查找test_*.py的文件，加载到测试套件中'''
#testdir="D:\EclipseWorkSapce\WebUIAutoTest\src\TestScript"
base_dir=str(os.path.dirname(__file__))

def createsuite():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(base_dir,pattern='test_*.py', top_level_dir=None)
    for test_suite in discover:
        for testsuit in test_suite:
            testunit.addTest(testsuit)
    return testunit


if __name__=="__main__":
    createsuite()
    
