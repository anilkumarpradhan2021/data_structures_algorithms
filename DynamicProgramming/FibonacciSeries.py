'''
Created on 18-Nov-2016

@author: anpradha
'''

'''T(n) = T(n-1) + T(n-2) + 1 = 2^n = O(2^n)'''


def fibo_using_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_using_recursion(n - 1) + fibo_using_recursion(n - 2) 

'''Time Com­plex­ity: O(n) , Space Com­plex­ity : O(n)  :

Dynamic Pro­gram­ming Approaches:
Bottom-Up Approach

'''


def fibo_using_dynamic_programming(n):
    temp = [0 for _ in range(n + 1)]
    
    temp[0] = 0
    temp[1] = 1
    
    for i in range(2, n + 1):
        temp[i] = temp[i - 1] + temp[i - 2]
    
    return temp[n]        


'''Time Com­plex­ity: O(n) , Space Com­plex­ity : O(1)  : '''

def fibo_without_recussion(n):
    if n == 0 or n == 1:
        return n
    else:
        f0 = 0 
        f1 = 1
        fn = 0
        for _ in range(2, n + 1):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return fn    

    
if __name__ == '__main__':
    print("Fibonacci using recurssion ")
    print(fibo_using_recursion(5))

    print("Fibonacci using DP ")
    print(fibo_using_dynamic_programming(5))

    print("Fibonacci without recurssion ")    
    print(fibo_without_recussion(5))
