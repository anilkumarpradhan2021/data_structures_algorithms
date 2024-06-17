'''
Created on 12-Aug-2019

@author: anpradha

Efficient program to print all prime factors of a given number
Given a number n, write an efficient function to print all prime factors of n. For example, 
if the input number is 12, then output should be “2 2 3”. 
    And 
if the input number is 315, then output should be “3 3 5 7”.

Following are the steps to find all prime factors.
1) While n is divisible by 2, print 2 and divide n by 2.
2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. While i divides n, print i and divide n by i, increment i by 2 and continue.
3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2.



'''

import math


def printAllPrimeFactor(num):
    if num > 0 :
        # Print the number of two's that divide n 
        while num % 2 == 0:
            num = num / 2
            print(2)

        # num must be odd at this point 
        # so a skip of 2 ( i = i + 2) can be used         
        for i in range(3, int(math.sqrt(num)) + 1, 2) :

        # while i divides num , print i ad divide num             
            while num % i == 0:
                print(i)
                num = num / i
                
        # Condition if num is a prime 
        # number greater than 2                 
        if num > 2:
            print(num)

    
if __name__ == '__main__':
    n = 121
    printAllPrimeFactor(n)
