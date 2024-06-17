'''
Created on 17-Nov-2019

@author: anpradha


Count ways to reach the n’th stair

There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. 
Count the number of ways, the person can reach the top.

More Examples:

Input: n = 1
Output: 1
There is only one way to climb 1 stair

Input: n = 2
Output: 2
There are two ways: (1, 1) and (2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)

We can easily find recursive nature in above problem. The person can reach n’th stair from either (n-1)’th stair or from (n-2)’th stair. Let the total number of ways to reach n’t stair be ‘ways(n)’. The value of ‘ways(n)’ can be written as following.

ways(n) = ways(n-1) + ways(n-2)

The above expression is actually the expression for Fibonacci numbers, but there is one thing to notice, the value of ways(n) is equal to fibonacci(n+1).

ways(1) = fib(2) = 1
ways(2) = fib(3) = 2
ways(3) = fib(4) = 3

Generalization of the above problem
How to count number of ways if the person can climb up to m stairs for a given value m? For example if m is 4, the person can climb 1 stair or 2 stairs or 3 stairs or 4 stairs at a time.

   ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... ways(n-m, m)
    
'''


# Recursive function used by countWays 
def countWaysUtil(n, m): 
    if n <= 1: 
        return n 
    res = 0
    i = 1
    while i <= m and i <= n: 
        res = res + countWaysUtil(n - i, m) 
        i = i + 1
    return res 

      
# Returns number of ways to reach s'th stair     
def countWays(s, m): 
    return countWaysUtil(s + 1, m) 


# Recursive function used by countWays 
def countWaysUtilDP(n, m): 
    res = [0 for x in range(n + 1)]  # Creates list res with all elements 0 
    res[0], res[1] = 1, 1
      
    for i in range(2, n + 1): 
        j = 1
        while j <= m and j <= i: 
            res[i] = res[i] + res[i - j] 
            j = j + 1 
    return res[n - 1] 


# Returns number of ways to reach s'th stair 
def countWaysDP(s, m): 
    return countWaysUtil(s + 1, m) 


if __name__ == '__main__':
    numberOfSteps, numberOfWays = 4, 2
    print("Number of ways =", countWays(numberOfSteps, numberOfWays))
    
