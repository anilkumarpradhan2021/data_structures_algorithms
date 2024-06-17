#!/usr/local/bin/python3.4
from pip._vendor.distlib.compat import raw_input


#Global Varible
AGE = 12
print("before ")

def testing():
    """
    comments if any 
    """
    print("ANyName "*10)

def function1(name):
    print("in function1")
    print("Your Name is  : %s " % name)
    
def function2(your_age, your_name):
    print("in function2")
    print("Your Name is : %s and age is : %s" % (name, age))

def function3(name, age='23'):
    print("in function3")
    print("Age is default")
    print("Your Name is : %s and age is : %s" % (name, age))
        

def function4(name, *age):
    print("in function4")
    print("Your Name is : %s" %name)
    for var in age:
        print("Var Age is  "  +str(var))

def modifyGlobalVariableAge(age):
    global AGE
    AGE = age
        
if __name__ == '__main__':
    name = raw_input("What is your name")
    age = raw_input("What is your age")
    print("My name is : " + name)
    testing()
    function1(name)
    function2(age, name)
    function2(your_name=name, your_age=age)
    function3(name)
    function4(name,12,23,3,3,3)
    print("Global Age is : %s" %AGE)
    modifyGlobalVariableAge(age)
    print("Modified Global Age is : %s" %AGE)
 
    # testing()    
