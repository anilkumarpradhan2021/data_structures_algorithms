'''
Created on 15-May-2017

@author: anpradha
'''
import unittest
class Test1(unittest.TestCase):
    def setUp(self):
        print("I am in setup")
    
    def tearDown(self):
        print("I am tear down")
     
    def test_first(self):
        print("Testing")
        self.assertEqual("Anil", "Anil", "Name not match")         
    
if __name__ == "__main__":
    unittest.main()   
    #python -m unittest fileName 