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

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for count in range(0, 6):
            with self.subTest(count=count):
                self.assertEqual(count % 2, 0)    
    
 
def suite_create():
    suite_obj = unittest.TestSuite()
    suite_obj.addTest(Test1("test_first"))
    suite_obj.addTest(Test1("test_even"))
    return suite_obj   

 
if __name__ == "__main__":
    unittest.main(verbosity=2)   
    #python -m unittest fileName 
    
    #===========================================================================
    # runner_obj = unittest.TextTestRunner()
    # test_suite = suite_create()
    # runner_obj.run(test_suite)
    #===========================================================================