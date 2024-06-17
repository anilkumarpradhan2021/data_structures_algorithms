'''
Created on 16-May-2017

@author: anpradha
'''
import random
import unittest
import HTMLTestRunner

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        self.assertEqual("Anil","Anil")

    @unittest.skip("Test Skipped1")
    def test_choicep(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
    @unittest.skip("Test Skipped2")
    def test_samplep(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


def suite_create():
    suite_obj = unittest.TestSuite()
    suite_obj.addTest(TestSequenceFunctions("test_shuffle"))
    return suite_obj   

if __name__ == "__main__":
    #unittest.main()   
    #python -m unittest fileName 
    runner_obj = unittest.TextTestRunner()
    test_suite = suite_create()
    runner_obj.run(test_suite)
    
    outfile = open("\\Users\\anpradha\\Documents\\eclipse_pyats\\Testing\\unittestExample\\Report.html", "w")   
#===============================================================================
#     outfile = open("\\Users\\anpradha\\Documents\\eclipse_pyats\\Testing\\unittestExample\\Report.html", "w")
#     runner = HTMLTestRunner.HTMLTestRunner(
#                     stream=outfile,
#                     title='Test Report',
#                     description='This demonstrates the report output by Anil.'
#                     )
# 
#     runner.run(test_suite)
#===============================================================================
    
    HTMLTestRunner.main()
