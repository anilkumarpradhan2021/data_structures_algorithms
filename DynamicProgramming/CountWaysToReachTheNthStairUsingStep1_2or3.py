'''
Created on 23-Nov-2019

@author: anpradha

Count ways to reach the nth stair using step 1, 2 or 3
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

There are two methods to solve this problem
1. Recursive Method
2. Dynamic Programming


https://www.geeksforgeeks.org/count-ways-reach-nth-stair-using-step-1-2-3/

'''
# A recursive function used by countWays 
def countWays(n) : 
    res = [0] * (n + 1) 
    res[0] = 1
    res[1] = 1
    res[2] = 2
      
    for i in range(3, n + 1) : 
        res[i] = res[i - 1] + res[i - 2] + res[i - 3] 
      
    return res[n] 

def countWays2(n) : 
    if n <= 2:
        return n 
    else:
        f0 = 0
        f1 = 1
        f2 = 2
        fn = 0
          
        for _ in range(3, n + 1) : 
            fn = f0 + f1 + f2 
            f0 = f1
            f1 = f2
            f2 = fn
          
        return fn



if __name__ == '__main__':
    n = 3
    print(countWays(n)) 
