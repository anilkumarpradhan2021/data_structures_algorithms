'''
Created on 17-Sep-2016

@author: anpradha
'''
class TestClass(object):
    '''
    Class documentation
    '''


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.z = 0
    
    def func1(self):
        print("test func")         
    
    def __repr__(self):
        return "x is " + str(self.x) + " and y is : " + str(self.y)    

    
class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return str(self.__dict__)

def add(a, b):
    return Coordinate(a.x + b.x , a.y + b.y)    

def sub(a, b):
    return Coordinate(a.x - b.x , a.y - b.y)    

def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        
        result = func(a, b)
        if result.x < 0 or result.y < 0:
            result = Coordinate(result.x if result.x > 0 else 0, result.y if result.y > 0 else 0)
             
        return result
    return checker

@wrapper
def add1(a, b):
    return Coordinate(a.x + b.x , a.y + b.y)    

@wrapper
def sub1(a, b):
    return Coordinate(a.x - b.x , a.y - b.y)    

if __name__ == '__main__':
    t = TestClass()
    print(t)
    print(dir(t))
    print(t.__dict__)        
    one = Coordinate(100, 200)
    two = Coordinate(300, 400)
    three = add(one, two) 
    print(three)
    four = sub(one, two)   
    print(four)
    print("Applying decorator here , means modify the add/sub function as per my requirement")
    add = wrapper(add)
    sub = wrapper(sub)
    four = sub(one, two)
    print(four)
    print("Applying decorator for sub1 and add1 using @ symbol")
    six = sub1(one,two)
    print(six)
    
