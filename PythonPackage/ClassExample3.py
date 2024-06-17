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
        return self.__dict__
    
    def __str__(self):
        return str(self.__dict__)  

    


if __name__ == '__main__':
    t = TestClass2()
    print(t)
