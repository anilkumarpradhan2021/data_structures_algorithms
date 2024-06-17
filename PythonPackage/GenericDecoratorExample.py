'''
Created on 17-Sep-2016

@author: anpradha
'''

def logger(func):
    print("Function Name : " + str(func))
    def inner(*args1, **args2):
        print("Arguments are : " + str(args1) + " : " + str(args2))
        return func(*args1, **args2) 
    return inner


@logger
def add(x, y):
    return x + y

@logger
def sub(x, y):
    return x - y

if __name__ == '__main__':
    print("--------")
    print(str(add(1, 3)))
    print("--------")
    print(add(5,6))
