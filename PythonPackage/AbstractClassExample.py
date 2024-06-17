'''
Created on 23-Aug-2019

@author: anpradha
'''
from abc import ABC, abstractclassmethod

class AbstractClassExample(ABC):
    def __init__(self):
        print("Nothing to print")
    
    @abstractclassmethod    
    def abstractMethod1(self):    
        pass

class ChildClassUseAbstractClass(AbstractClassExample):
    
    def test1(self):
        print("I am in test1")
    
    def abstractMethod1(self):
        print("I am a abstract method defined in child class")   
        
if __name__ == '__main__':
    #a = AbstractClassExample()
    c = ChildClassUseAbstractClass()
    c.test1()
    c.abstractMethod1()