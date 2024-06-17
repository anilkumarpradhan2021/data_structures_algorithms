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
     
    def runTest (self):

        """ Test addition and succeed. """

        self.failUnless (1+1==2, "one plus one fails!")

        self.failIf (1+1 != 2, "one plus one fails again!")

        self.failUnlessEqual (1+1, 2, "more trouble with one plus one!")

 
def suite_create():
    suite_obj = unittest.TestSuite()
    suite_obj.addTest(Test1())
    return suite_obj   

 
if __name__ == "__main__":
    #unittest.main()   
    #python -m unittest fileName 
    runner_obj = unittest.TextTestRunner()
    test_suite = suite_create()
    runner_obj.run(test_suite)