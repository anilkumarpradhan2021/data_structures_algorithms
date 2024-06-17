'''
Created on 03-Jan-2018

@author: anpradha
'''
# tests.py
import unittest
from ddt import ddt, data
from unittestExample import HTMLTestRunner

 
@ddt
class FooTestCase(unittest.TestCase):
    a = [1,2,34]
    @data(a)
    def test_larger_than_two(self, value):
        print("Hi : ")
        print(value)
 
if __name__ == '__main__':
    unittest.main() 
 