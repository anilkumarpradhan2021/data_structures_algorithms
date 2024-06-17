'''
Created on 14-Nov-2019

@author: anpradha

Ways to sum to N using array elements with repetition allowed
Given a set of m distinct positive integers and a value ‘N’. The problem is to count the total number of ways we can form ‘N’ by doing sum of the array elements. Repetitions and different arrangements are allowed.

Examples :

Input : arr = {1, 5, 6}, N = 7
Output : 6

Explanation:- The different ways are:
1+1+1+1+1+1+1
1+1+5
1+5+1
5+1+1
1+6
6+1

Input : arr = {12, 3, 1, 9}, N = 14
Output : 150

Very Easy One 

Time Complexity: O(N*m)


https://www.geeksforgeeks.org/ways-sum-n-using-array-elements-repetition-allowed/


NOTE:
Its the opposite of minimum number of coin required for a number (coin - change problem , its done in DynamicProgramming section)

'''

# Function to count the total  
# number of ways to sum up to 'N' 
def countWays(arr, m, N): 
  
    count = [0 for i in range(N + 1)] 
      
    # base case 
    count[0] = 1
      
    # Count ways for all values up  
    # to 'N' and store the result 
    print(count)
    for i in range(1, N + 1): 
        for j in range(m): 
  
            # if i >= arr[j] then 
            # accumulate count for value 'i' as 
            # ways to form value 'i-arr[j]' 
            if (i >= arr[j]):
                count[i] = count[i]  + count[i - arr[j]] 
        print(count)
      
    # required number of ways
    return count[N] 


      

if __name__ == '__main__':
    arr = [1, 5, 6] 
    m = len(arr) 
    N = 7
    print("Total number of ways = ", 
               countWays(arr, m, N)) 

    arr = [12, 3, 1, 9] 
    m = len(arr) 
    N = 14
    print("Total number of ways = ", 
               countWays(arr, m, N)) 
