'''
Created on 13-Oct-2016
Problem :

Add one to a number represented as an array of digits


@author: anpradha
'''

def addOne(number):
    carry = 1
    for i in range(len(number) - 1, -1, -1):
        val = number[i] + carry
        number[i] = val % 10
        carry = val // 10
    
    if carry == 1:
        number.insert(0, carry)    
        
    print(number)    
        
if __name__ == '__main__':
    number = [9, 0]
    addOne(number)
