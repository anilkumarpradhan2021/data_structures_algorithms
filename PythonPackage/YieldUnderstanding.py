'''
Created on 03-Oct-2016

@author: anpradha
'''


def yield_test():
    arr = [1, 2, 3]
    for i in arr:
        yield i
    
if __name__ == '__main__':
    a = yield_test()
    for i in a:
        print(i) 
        
    for i in a:
        print("test")
        print(i) 
    