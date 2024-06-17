'''
Created on 04-Dec-2019

@author: anpradha
'''


def decoratorUI(func):
    def wrap(*args, **kwargs):
        retval = func(*args,**kwargs)
        return retval

    return wrap


@decoratorUI
def test(*args, **kwargs):
    print(args)
    print(*kwargs)

def decorator_function(func):
    def inner_docorator_function(**args):
        print("Hi Why")
        return func(*args)
    return inner_docorator_function    

@decorator_function
def test_decorator(*args, **kwargs):
    print("Hi")
    print(args)
    print(kwargs)
    
if __name__ == '__main__':
    test(a=1, b=2, c=3)
    test_decorator(a="anil")
