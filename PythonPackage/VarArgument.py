'''
Created on 17-Sep-2016

@author: anpradha
'''

def add(a, b):
    return a + b

''' List '''
def var_args(*args):
    print(args)
    return args


'''
    dictionary
'''
def var_args2(**args):
    print(args)
    return args

if __name__ == '__main__':
    arr = [1, 2]
    dict_temp = {'x':1, 'y':2}
    
    print("add(arr[0], arr[1]) : " + str(add(arr[0], arr[1])))
    print("add(*arr) : " + str(add(*arr)))
    
    print("var_args() : " + str(var_args()))
    print("var_args(1,2) : " + str(var_args(1, 2)))
    print("var_args(*arr) : " + str(var_args(*arr)))
    print("var_args(1,2,3,5) : " + str(var_args(1, 2, 3, 5)))
    
    print("var_args2() : " + str(var_args2()))
    print("var_args2(**dict_temp) : " + str(var_args2(**dict_temp)))
    print("add(*dict_temp.values()) : " + str(add(*dict_temp.values())))
    print("add(*dict_temp) : " + str(add(*dict_temp)))
    
    
