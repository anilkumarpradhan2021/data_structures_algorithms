'''
Created on 23-Sep-2019

@author: anpradha

Given an array arr[] of size n containing integers. The problem is to find the length of the longest sub-array having sum equal to the given value k.

Examples:

Input : arr[] = { 10, 5, 2, 7, 1, 9 }, 
            k = 15
Output : 4
The sub-array is {5, 2, 7, 1}.

Input : arr[] = {-5, 8, -14, 2, 4, 12},
            k = -5
Output : 5


Efficient Approach: Following are the steps:

1. Initialize sum = 0 and maxLen = 0.
2. Create a hash table having key  = sum and value = index
For i = 0 to n-1, perform the following steps:
1. Accumulate arr[i] to sum.
2. If sum == k, update maxLen = i+1.
3. Check whether sum is present in the hash table or not. If not present, then add it to the hash table as (sum, i) pair.
4. Check if (sum-k) is present in the hash table or not. If present, then obtain index of (sum-k) from the hash table as index. Now check if maxLen < (i-index), then update maxLen = (i-index).
Return maxLen.

'''


def logestSubArrayHavingSumK(arr, k):
    d = {}
    update_sum = 0
    max_sub_arry_length = -1
    for i in range(len(arr)):
        
        update_sum = update_sum + arr[i]
        
        # As index starts from 0 then actual length is i+1 
        if update_sum == k:
            max_sub_arry_length = max(i + 1, max_sub_arry_length)
        
        # Add the update_sum to dictionary
        if update_sum not in d:
            d[update_sum] = i 
        
        # Check if update_sum - k keys is present , that means already we have a entry where update_sum == k
        if update_sum - k in d:
            max_sub_arry_length = max(i - d[update_sum - k], max_sub_arry_length)

    print(max_sub_arry_length)

    
if __name__ == '__main__':
    arr = [10, 5, 2, 7, 1, 9]
    k = 15
    logestSubArrayHavingSumK(arr, k)
    
    arr = [-5, 8, -14, 2, 4, 12]
    k = -5
    logestSubArrayHavingSumK(arr, k)
    
    arr = [1, 4, 0, 0, 3, 10, 5]
    k = 7
    logestSubArrayHavingSumK(arr, k)
    
    arr = [1, -1, 1, 1, 1, -1, -1]
    k = 0
    logestSubArrayHavingSumK(arr, k)
    
