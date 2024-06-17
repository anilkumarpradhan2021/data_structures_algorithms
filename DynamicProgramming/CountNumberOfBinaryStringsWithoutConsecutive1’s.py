'''
Created on 17-Nov-2019

@author: anpradha


Count number of binary strings without consecutive 1’s

Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s.

Examples:

Input:  N = 2
Output: 3
// The 3 strings are 00, 01, 10

Input: N = 3
Output: 5
// The 5 strings are 000, 001, 010, 100, 101


Its actually a fibonacy series , so 1st manully find for n=1 and n=2 then , apply the rule

https://www.youtube.com/watch?v=a9-NtLIs1Kk&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=39

If we take a closer look at the pattern, we can observe that the count is actually (n+2)’th Fibonacci number for n >= 1. The Fibonacci Numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, ….

n = 1, count = 2  = fib(3)
n = 2, count = 3  = fib(4)
n = 3, count = 5  = fib(5)
n = 4, count = 8  = fib(6)
n = 5, count = 13 = fib(7)


'''


def count(n):
    aux = [0 for i in range(n + 1)]
    aux[1] = 2
    aux[2] = 3
    
    for i in range(3, n + 1):
        aux[i] = aux[i - 1] + aux[i - 2]
    return aux[4]    

    
if __name__ == '__main__':
    print(count(4))
