'''
Created on 23-Sep-2019

@author: anpradha
'''


def swap1(a, b):
    print("a ,b" , a, b)
    a = a + b 
    b = a - b 
    a = a - b
    print("a ,b" , a, b)

    
def swap2(a, b):
    print("a ,b" , a, b)
    a = a ^ b 
    b = a ^ b 
    a = a ^ b
    print("a ,b" , a, b)

    
if __name__ == '__main__':
    swap1(10, 20)
