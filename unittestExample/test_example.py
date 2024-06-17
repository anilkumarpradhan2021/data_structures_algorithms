'''
Created on 06-Sep-2016

@author: anpradha
'''
import unittest
from unittestExample import HTMLTestRunner
from UseTestMathPackage.Testing import assert_equal
import sys
'''
The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method. 
'''


def sum(x, y):
    return x + y


class TestSum(unittest.TestCase):
    def setUp(self):
        print("Just a setup section")

    def test_sum(self): 
        print("I am in test1 Section")
        assert_equal(sum(1, 2), 3)

    def test_sum2(self): 
        print("I am in test2 Section")
        assert_equal(sum(1, 2), 3)

    def tearDown(self):
        print("Just a tear Down section")

    
if __name__ == '__main__':
    HTMLTestRunner.main()
    #unittest.main()
    
    
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestSum)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    
