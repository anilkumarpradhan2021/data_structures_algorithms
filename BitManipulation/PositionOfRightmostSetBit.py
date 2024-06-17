'''
Created on 22-Nov-2019

@author: anpradha

Position of rightmost set bit
Write a one line function to return position of first 1 from right to left, in binary representation of an Integer.

I/P    18,   Binary Representation 010010
O/P   2
I/P    19,   Binary Representation 010011
O/P   1



'''
import math 

  
def getFirstSetBitPos(n): 
  
    return int(math.log2(n & -n)) + 1
 
  
def getFirstSetBitPos2(n): 
  
    return (n & -n)


if __name__ == '__main__':
    print(getFirstSetBitPos(18))
    print(getFirstSetBitPos2(18))
