'''
Created on 26-Sep-2016

@author: anpradha

Write a program to calculate pow(x,n)
'''

'''
Time Complexity: O(n)
Space Complexity: O(1)
Algorithmic Paradigm: Divide and conquer.

'''
def power1(x, n):
    temp = 1
    if n == 0:
        return 1
    for i in range(n):
        temp = temp * x 
    return temp

'''
Time Complexity: O(n)
'''
def power2(x, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return power2(x, n // 2) * power2(x, n // 2)
        else:
            return x * power2(x, n // 2) * power2(x, n // 2)
         


''' 
Time Complexity: O(n)
Space Complexity: O(1)
Algorithmic Paradigm: Divide and conquer.

Above function can be optimized to O(logn) by calculating power(x, y/2) only once and storing it.

'''
def power3(x, n):
    if n == 0:
        return 1
    else:
        temp = power3(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp


'''
Time Complexity of optimized solution: O(logn)
Let us extend the pow function to work for negative y and float x.

'''
def power4(x, n):
    if n == 0:
        return 1
    
    if n == -1:
        return 1 / x
    else:
        temp = power4(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return x * (temp * temp) 
            
             
if __name__ == '__main__':
    x = 2
    n = 1
    print(power1(x, 3))
    print(power2(x, 3))
    print(power3(x, 3))
    print(power4(x, -3))
     
