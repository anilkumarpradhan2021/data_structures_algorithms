'''
Created on 18-Sep-2016

@author: anpradha
'''

class decoratorWithoutArguments(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__() - step-1")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print("Inside __call__() -step-4")
        self.f(*args)
        print("After self.f(*args) -step-6")

@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print ("After decoration - step-2")
print ("Preparing to call sayHello() -step-3")
sayHello("say", "hello", "argument", "list - -step-5")  #step -5
print ("After first sayHello() call -step-7")
sayHello("a", "different", "set of", "arguments -step-5") # repeat from step-4,function-5,6
print ("After second sayHello() call -step-7") 


if __name__ == '__main__':
    pass
