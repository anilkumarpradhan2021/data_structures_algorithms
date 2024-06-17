'''
Created on 12-Oct-2016

@author: anpradha
'''

'''
It will check for kth bit , if kth bit is 1 return 1 else return 0
'''


def checkIfKthBitIsOnOrOff(n, k):
    if n & (1 << (k - 1)):
        return 1
    else:
        return 0


''' Let consider its 32 bit so from left to right just print the bit'''


def decimal_to_binary(number):
    
    ''' Lets its 32 bit number'''
    
    for i in range(31, 0, -1):
        print(checkIfKthBitIsOnOrOff(number, i), end=' ')
    print()    


def decimalToBinary(num):
    b = ""
    while num > 0:
        if num %2==0:
            b = "0" + b
        else:
            b = "1" + b
                 
        num = num // 2 

    print(b)
        
if __name__ == '__main__':
    decimal_to_binary(4)
    decimal_to_binary(16)  
    decimal_to_binary(100)  
    
    decimalToBinary(100)  
