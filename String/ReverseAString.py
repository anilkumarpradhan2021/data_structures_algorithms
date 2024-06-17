'''
Created on 01-Sep-2016

@author: anpradha
'''
from operator import xor


def reverseString(string):
    temp = list(string)
    print("String is : " + str(temp))
    for i in range(len(temp) // 2):
        # t = temp[i]
        # temp[i] = temp[len(temp) - 1 - i]
        # temp[len(temp) - 1 - i] = t
        
        '''
        Python Program to Swap Variables Without Temporary Variable
        
        without using any extra variable (temp variable)
        e.g 
        x,y = y,x
        s
        '''
        
        temp[i] , temp[len(temp) - 1 - i] = temp[len(temp) - 1 - i], temp[i]
    print("Reserve String is : " + str(temp))   
    
    
def reverse_string(str):
    t = ""
    for i in str:
        t = i + t
    return t


def reverse_string2(str):
    n = len(str) - 1
    i = 0
    str = list(str)
    while i < n:
        str[i], str[n] = str[n] , str[i]
        i = i + 1
        n = n - 1
        
    return "".join(str)

         
if __name__ == '__main__':
    pass
    reverseString("Anil")
    test = list("Anil")
    print(test[::-1])
    print(reverse_string("Anil"))
    print(reverse_string2("Anil"))
