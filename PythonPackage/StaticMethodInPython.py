'''
Created on 16-Aug-2016

@author: anpradha



A class method takes cls as first parameter while a static method needs no specific parameters.
A class method can access or modify class state while a static method can’t access or modify it.
In general, static methods know nothing about class state. They are utility type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.


'''

class StaticClassExample(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    '''
    We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor ) for different use cases.
    '''    
    @classmethod
    def static_method(cls):
        print("Hi I am a class method")  
    
    '''We generally use static methods to create utility functions.'''    
    @staticmethod
    def static_method1():
        print("I am a static method")
      
        
if __name__ == '__main__':
    StaticClassExample.static_method()
    StaticClassExample.static_method1()