'''
Created on 25-Sep-2019

@author: anpradha
'''

import math


def findMSB(n):
    
    if n == 0:
        return 0
    # find the log of n with base 2  
    
    # To find the position of 
    # the most significant  
    # set bit 
    k = int(math.log(n, 2)) 
      
    # To return the value  
    # of the number with set  
    # bit at k-th position 
    return 2 ** k 


''' Logic is divide the number by 2 till become 0 '''


def findMsb(n):
    if n == 0:
        return 0
    
    c = 0
    while n > 0:
        c = c + 1
        n = n >> 1
    return 2 ** (c - 1)    

    
if __name__ == '__main__':
    print(findMSB(11))
    print(findMsb(11))
    print(findMSB(0))
    print(findMsb(0))
    
