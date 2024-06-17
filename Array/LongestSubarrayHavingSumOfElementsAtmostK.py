'''
Created on 23-Sep-2019

@author: anpradha

Longest Subarray having sum of elements atmost ‘k’
Given an array of integers, our goal is to find the length of largest subarray having sum of its elements atmost ‘k’ where k>0.

Examples:

Input : arr[] = {1, 2, 1, 0, 1, 1, 0}, 
           k = 4
Output : 5
Explanation:
 {1, 2, 1} => sum = 4, length = 3
 {1, 2, 1, 0}, {2, 1, 0, 1} => sum = 4, length = 4
 {1, 0, 1, 1, 0} =>5 sum = 3, length = 5



'''


def atMostSum(arr, k): 
    max_length = float("-inf")
    currrnt_sum = 0
    count = 0
    for i in range(len(arr)):
        if currrnt_sum + arr[i] > k:
            currrnt_sum = currrnt_sum - arr[i - count] 
        else:
            count = count + 1
        max_length = max(max_length, count)    
        currrnt_sum = currrnt_sum + arr[i]
    print("Count : " , count)
    print("max_length: " , max_length)    
        

def atMostSum2(arr, k): 
    max_length = float("-inf")
    currrnt_sum = 0
    count = 0
    for i in range(len(arr)):
        if currrnt_sum + arr[i] <= k:
            currrnt_sum = currrnt_sum + arr[i]
            count = count + 1
        else:
            currrnt_sum = currrnt_sum + arr[i] - arr[i-count]
        max_length = max(max_length, count)    
    print("Count : " , count)
    print("max_length: " , max_length)    

if __name__ == '__main__':
    arr = [1, 2, 1, 0, 1, 1, 0]
    k = 4
    atMostSum(arr, k)
    atMostSum2(arr, k)
