'''
Created on 24-Sep-2019

@author: anpradha


Find value of k-th bit in binary representation
Given a number n and k (1 <= k <= 32), find value of k-th bit in binary representation of n. Bits are numbered from right (Least Significant Bit) to left (Most Significant Bit).

Examples :

Input :  n = 13, k = 2
Output : 0
Binary representation of 13 is 1101.
Second bit from right is 0.

Input :  n = 14, k = 3
Output : 1
Binary representation of 14 is 1110.
Third bit from right is 1.


Note :
we clear all bits other than the bit at bit i. Finally, we compare that to 0. If that new value is not zero,
then bit i must have a 1. Otherwise, biti is a 0.

'''


def findBit(n, k):
    return 1 if n & (1 << k - 1) != 0 else 0


if __name__ == '__main__':
    n = 7 
    k = 1
    
    n = 8
    k = 1
    
    print(findBit(n, k))
