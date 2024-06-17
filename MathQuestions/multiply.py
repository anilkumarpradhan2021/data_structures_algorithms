#!/usr/local/bin/python3.4

'''
Created on 10-Apr-2016

@author: anpradha
'''


def mul(a, b):
    result = 0
    while b > 0:
        if b & 1 == 1:
            result = result + a
        a = a << 1
        b = b >> 1    
    return result


if __name__ == '__main__':
    a = 10
    b = 10
    print(mul(a, b))
