'''
Created on 13-Oct-2016

@author: anpradha


Problem :

Rearrange positive and negative numbers

Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array without using 
any additional data structure like hash table, arrays, etc. The order of appearance should be maintained.

Examples:

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]

Complexity :O(n log n)

'''


'''
    Merges two subarrays of arr[].
    First subarray is arr[l..m] 
    Second subarray is arr[m+1..r]
'''
def merge(arr, l, m, r):
    
    '''Initial index of 1st subarray'''
    i = l
    '''Initial index of IInd'''
    j = m + 1  
    
    '''arr[l..i] is negative ,  arr[i..m] is positive'''
    while i <= m and arr[i] < 0:
        i += 1
     
    '''arr[mid+1..j-1] is negative  , arr[j..r] is positive'''    
    while j <= r and arr[j] < 0:
        j += 1
    
    '''reverse positive part of left sub-array (arr[i..m])'''    
    reverse(arr, i, m)
    
    '''reverse negative part of right sub-array (arr[m+1..j-1])'''
    reverse(arr, m + 1, j - 1)
    
    '''reverse arr[i..j-1]'''
    reverse(arr, i, j - 1)
    
    
def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)    



if __name__ == '__main__':
    arr = [1, -2, 3, -4, 5 , -6, 7, -8, 9, -10 ]
    print("Array Before Sort : " + str(arr))
    mergeSort(arr, 0, len(arr) - 1)
    print("Array after Sort : " + str(arr))
