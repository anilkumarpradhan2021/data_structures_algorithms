'''
Created on 13-March-2021

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



if __name__ == '__main__':
    s = ObjectCreateValidationExample("Anil" , 0)
    print(s)
    print(s.name)
    
    
