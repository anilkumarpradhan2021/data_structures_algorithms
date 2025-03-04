'''
Created on 18-Sep-2016

@author: anpradha
'''

'''
Created on 17-Sep-2016

@author: anpradha
'''
class TestClass2(object):
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
        print("I am in repr")
        return f"TestClass2(x='{self.x}', y={self.y},z='{self.z}')"
    
    def __str__(self):
        print("I am in str")
        return str(self.__dict__)  

    


if __name__ == '__main__':
    t = TestClass2()
    print(t)
    print("Eval will call repr")
    print(repr(t))