'''
Created on 23-Sep-2019

@author: anpradha

Count trailing zeroes in factorial of a number
Given an integer n, write a function that returns count of trailing zeroes in n!.
Examples :

Input: n = 5
Output: 1 
Factorial of 5 is 120 which has one trailing 0.

Input: n = 20
Output: 4
Factorial of 20 is 2432902008176640000 which has
4 trailing zeroes.

Input: n = 100
Output: 24


https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/


'''


def countTrailingZeroesInFactorialOfNumber(n):
    i = 5
    count = 0
    while n // i > 0:
        count = count + n // i 
        i = i * 5

    print(count)


def zeros(n):
    count = 0
    while n > 0:
        count = count +  n // 5
        n = n / 5
    print(count)

if __name__ == '__main__':
    n = 100
    countTrailingZeroesInFactorialOfNumber(n)
    zeros(n)
    