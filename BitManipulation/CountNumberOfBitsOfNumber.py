'''
Created on 25-Sep-2019

@author: anpradha

Count total bits in a number
Given a positive number n, count total bit in it.

Examples:

Input : 13
Output : 4
Binary representation of 13 is 1001

Input  : 183
Output : 8

Input  : 4096
Output : 13


'''

'''
2^n = num
log(2^n) = log(num)
nlog2 = log(num)
n = log(num) / log(2)

'''

import math


def countBitsUsingLog(num):
    return (math.log(num, 10) // math.log(2, 10)) + 1


def countBits(num):
    count = 0
    while num > 0 :
        count = count + 1
        num = num >> 1

    return count


if __name__ == '__main__':
    print(countBits(13))
    print(countBits(183))
    print(countBits(4096))
    print()
    print(countBitsUsingLog(13))
    print(countBitsUsingLog(183))
    print(countBitsUsingLog(4096))

