'''
Created on 17-Sep-2016

@author: anpradha
'''

class myDecorator(object):

    def __init__(self, f):
        print("inside myDecorator.__init__()")
        self.f = f

    def __call__(self):
        print("Entering function : " +str(self.f.__name__))
        self.f()
        print("Existed function : " +str(self.f.__name__))
        


@myDecorator
def aFunction():
    print ("inside aFunction()")

if __name__ == '__main__':
    aFunction()
