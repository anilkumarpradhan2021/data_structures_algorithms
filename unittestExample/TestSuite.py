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
        self.assertEqual("Anil", "Anil1", "Name not match")         

    
    
 
def suite_create():
    suite_obj = unittest.TestSuite()
    suite_obj.addTest(Test1("test_first"))
    
    return suite_obj   

 
if __name__ == "__main__":
    #unittest.main()   
    #python -m unittest fileName 
    runner_obj = unittest.TextTestRunner()
    test_suite = suite_create()
    runner_obj.run(test_suite)