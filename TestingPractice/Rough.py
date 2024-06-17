'''
Created on 09-Aug-2018

@author: anpradha
'''
import datetime


class A():
    
    __instance = None
    
    def __init__(self):
        if A.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            A.__instance = self

    @staticmethod
    def getInstance():
        if A.__instance is None:
            A()
        return A.__instance    
        print("I am in Test")

if __name__ == '__main__':
    #print(A.getInstance())
    a = A()
    print(repr(a))

    print(A.getInstance())
    