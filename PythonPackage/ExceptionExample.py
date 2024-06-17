#!/usr/local/bin/python3.4


class UserDefinedException(Exception):
    def __init__(self, message):
        self.error_message = message
        
    
    def __str__(self):
        return Exception.__str__(self)    
         
    
def function1():
    try:
        raise IOError
    except IOError:
        print("Error happened")

def function2():
    try:
        raise 
    except:
        print("Bad Error  handle ")
    
def function3():
    try:
        raise RuntimeError
    except (IOError, RuntimeError):
        print("Error  handle for multiple type ")


def function4():
    try:
        raise RuntimeError
    except (IOError):
        print("Error  handle for multiple type ")

    except (RuntimeError):
        print("Error  handle for multiple type ")
    else:
        print("This section execute if no error occured in try block")
        
    finally:
        print("This section execute at the end")
        
def function5():
    try:
        raise UserDefinedException("Its a user defined exception")
    except (UserDefinedException):
        print("Error happened")
        raise UserDefinedException("Its a user defined exception")

def function6():
    try:
        raise RuntimeError
    except:
        print("Error  handle for multiple type ")
    else:
        print("This section execute if no error occured in try block")
        
    finally:
        print("This section execute at the end")


def function7():
    try:
        raise RuntimeError(1, 2)
    except RuntimeError as runtime:
        print("Error  handle for multiple type ")
        print("Argument are : " + str(runtime.args))
    else:
        print("This section execute if no error occured in try block")
        
    finally:
        print("This section execute at the end")
                
if  __name__ == '__main__' :
    function7()
    
