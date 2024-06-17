'''
Created on 11-Apr-2016

@author: anpradha
'''

class MyClass(object):
    '''
    Define all related document related to class
    '''

# Class level variable just like static in java
    AGE = 20

    def __init__(self, name, addres):
        self.name = name 
        self.address = addres
       
    def printInstantVariable(self):
        print("Your Name is : %s" % self.name)
        print("Its a instance variable")
        print("Your Address is : %s" % self.address)
        
       

    def printClassLevelvariable(self):
        print("Its a Class level variable")
        print("Your Age is : %s" % MyClass.AGE)
        
    def addNewnstanceVariable(self, roll):
        self.roll = roll       

    def printAllVariables(self):
        print("************* In print all Variable function : ************")
        class_name = self.__class__
        print("Class Name is :" + str(class_name))
        print("your Name : %s" % self.name)
        print("your Age : %s" % MyClass.AGE)
        print("your Address : %s" % self.address)
        print("your roll : %s" % self.roll)
        
        

if __name__ == '__main__':
    # create object of class MyClass
    name = input("Enter your name")
    address = input("Enter your address")
    test = MyClass(name, address)
    # Print instance variables
    test.printInstantVariable()
    # print class level variable
    test.printClassLevelvariable()    
    # add a new instance variable
    roll = input("Please enter your roll")
    test.addNewnstanceVariable(roll)
    test.printAllVariables()
    
    # Name of class
    print("Object information object.__dict__ : " + str(test.__dict__))
    print("Info about Class declaration about the class MyClass.__dict__ :  " + str(MyClass.__dict__))
    print("Module name where the class is defined : MyClass.__module__ :  " + str(MyClass.__module__))
    print("Class Documentation : MyClass.__doc__ : " + str(MyClass.__doc__))
    print("Base class for Class : MyClass.__bases__ : " + str(MyClass.__bases__))
    print("Print all the properties of the class in dictionary text format : dir(MyClass) : " + str(dir(MyClass))) 
               
