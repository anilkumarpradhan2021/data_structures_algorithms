'''
Created on 23-Nov-2019

@author: anpradha
Find subarray with given sum | Set 1 (Nonnegative Numbers)
Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
Examples :

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Complexity Analysis:  

Time Complexity : O(n). 
Only one traversal of the array is required. So the time complexity is O(n).
Space Complexity: O(1). 
As constant extra space is required.


'''


def subArraySum(arr, n, sum): 
      
    curr_sum = arr[0] 
    start = 0
  
    # Add elements one by  
    # one to curr_sum and  
    # if the curr_sum exceeds  
    # the sum, then remove  
    # starting element  
    i = 1
    while i <= n: 
          
        # If curr_sum exceeds 
        # the sum, then remove 
        # the starting elements 
        while curr_sum > sum and start < i - 1: 
            curr_sum = curr_sum - arr[start] 
            start += 1
              
        # If curr_sum becomes 
        # equal to sum, then 
        # return true 
        if curr_sum == sum: 
            print ("Sum found between indexes") 
            print ("%d and %d" % (start, i - 1)) 
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
  
    # If we reach here,  
    # then no subarray 
    print ("No subarray found") 
    return 0


def subArraySum2(arr, sum): 
      
    curr_sum = arr[0] 
    start = 0

    for i in range(1,len(arr)):
        while curr_sum > sum and start < i: 
            curr_sum = curr_sum - arr[start] 
            start = start + 1
              
        if curr_sum == sum: 
            print ("Sum found between indexes" , "%d and %d" % (start, i - 1)) 
            return 1
  
        curr_sum = curr_sum + arr[i] 
  
    print ("No subarray found") 
    return 0

                
if __name__ == '__main__':
    arr = [1, 4, 20, 3, 10, 5]
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    #subArraySum(arr, len(arr), 23)
    subArraySum2(arr, 23)
