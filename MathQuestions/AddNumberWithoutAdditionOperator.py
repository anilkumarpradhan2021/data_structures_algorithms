'''
Created on 19-Apr-2017

@author: anpradha

https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/

Add two numbers without using arithmetic operators
Write a function Add() that returns sum of two integers. The function should not use any of the arithmetic operators (+, ++, –, -, .. etc).
Sum of two bits can be obtained by performing XOR (^) of the two bits. Carry bit can be obtained by performing AND (&) of two bits.
Above is simple Half Adder logic that can be used to add 2 single bits. We can extend this logic for integers. 

If x and y don’t have set bits at same position(s), then bitwise XOR (^) of x and y gives the sum of x and y. 

To incorporate common set bits also, bitwise AND (&) is used. Bitwise AND of x and y gives all carry bits. 
We calculate (x & y) << 1  and add it to x ^ y to get the required result.
'''


def add(x, y):
    print(x , " : ", bin(x))
    print(y , ": " , bin(y))
        
    while(y):
        carry = x & y
        print("Carry is : " + bin(carry))
        print("Carry is : " + str(carry))
        x = x ^ y
        print("X is : " + str(x))
        y = carry << 1
        print("Y is : " + bin(y))
        print("Y is : " + str(y))
    return x    


if __name__ == '__main__':
    #print(add(151, 121))
    print(add(3,3))
