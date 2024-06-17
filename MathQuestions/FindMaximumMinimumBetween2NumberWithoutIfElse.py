'''
Created on 27-Sep-2019

@author: anpradha

Compute the minimum or maximum of two integers without branching



Method 1(Use XOR and comparison operator)

Minimum  : y ^ ((x ^ y) & -(x < y))

Maximum : x ^ ((x ^ y) & -(x < y));

'''


def findMin(a, b):
    return a * bool(b // a) + b * bool(a // b)


def findMax(a, b):
    return a * bool(a // b) + b * bool(b // a)



if __name__ == '__main__':
    a = 15
    b = 30
    print("Min : " , findMin(a, b))
    print("Max : " , findMax(a, b))
