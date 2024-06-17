'''
Created on 11-May-2016

@author: anpradha
'''

import os

if __name__ == '__main__':
    print(os.path.dirname(__file__))  # relative directory path
    print(os.path.abspath(__file__))  # absolute file path
    print(os.path.basename(__file__))  # the file name only    
    
    
    # remove file if exists
    filename = "/Users/anpradha/Desktop/Log.txt"
    try:
        os.remove(filename)
        print("File removed")
    except OSError:
        print("File not present")
        pass    
    
    print(os.path.isfile("/Users/anilpradhan/Desktop/eclipse_pyats/PythonAlgoProject/PythonPackage/Test.py"))