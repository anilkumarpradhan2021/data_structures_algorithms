'''
Created on 17-Sep-2019

@author: anpradha
'''

'''
This class is used for validating the salary  before creating the object 

'''


class ObjectCreateValidationExample():

    def __new__(cls, name, salary):
        if 0 < salary < 10000:
            return object.__new__(cls)
        else:
            print("Please correct the salary range between 0 to 10000")
            return None
        
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


if __name__ == '__main__':
    s = ObjectCreateValidationExample("Anil" , 10)
    print(s)
    print(s.name)
    
    a = Singleton()
    print(a.__dict__)
    
    a1 = Singleton()
    print(a1.__dict__)
    
