'''
Created on 06-Sep-2016

@author: anpradha
'''
import unittest
from unittestExample import HTMLTestRunner
from UseTestMathPackage.Testing import assert_equal
import sys
from ddt import ddt, data
import datetime
'''
The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method. 
'''


def sum(x, y):
    return x + y

@ddt
class TestSum(unittest.TestCase):
    def setUp(self):
        print("Just a setup section")

    def test_sum(self): 
        print("I am in test1 Section")
        assert_equal(sum(1, 2), 3)
        
    @data(1,2,43)    
    def test_sum2(self): 
        print("I am in test2 Section")
        assert_equal(sum(1, 2), 3)

    def tearDown(self):
        print("Just a tear Down section")

    
if __name__ == '__main__':
    #HTMLTestRunner.main()
    home_page_test = unittest.TestLoader().loadTestsFromTestCase(TestSum)
    
    # create a test suite combining search_text and home_page_test
    test_suite = unittest.TestSuite([home_page_test])

    file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.html")
    output = open(file_name, "wb")
    runner = HTMLTestRunner.HTMLTestRunner_BackUp(stream = output, verbosity = 1, title="Regression Suite")
    runner.run(test_suite)
 