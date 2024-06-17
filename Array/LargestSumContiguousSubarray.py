'''
Created on 09-Oct-2019

@author: anpradha
Largest Sum Contiguous Subarray
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

    Lets take the example:
    {-2, -3, 4, -1, -2, 1, 5, -3}

    Maximum contiguous sum is 7



'''

if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    
    max_sum = float("-inf")
    current_sum = 0
    
    for i in arr:
        current_sum = max(current_sum + i , i)
        max_sum = max(max_sum, current_sum)
    print(max_sum)    
