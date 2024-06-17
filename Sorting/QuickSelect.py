'''
Created on 09-Sep-2019

@author: anpradha


Quickselect Algorithm
Quickselect is a selection algorithm to find the k-th smallest element in an unordered list. It is related to the quick sort sorting algorithm.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}
           k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
           k = 4
Output: 10
The algorithm is similar to QuickSort. The difference is, instead of recurring for both sides (after finding pivot), 
it recurs only for the part that contains the k-th smallest element. 

The logic is simple, 

if pivot > k, then we recur for left part. 
If pivot == k we have found the k-th smallest element and we return. 
If pivot < k, then we recur for right part. 

This reduces the expected complexity from O(n log n) to O(n), with a worst case of O(n^2).

ASSUMPTION : NO DUPLICATE ELEMENTS IN ARRAY

'''


'''
Easy partition 


'''
def partition(arr, left, right):
    pivot = (left + right) // 2
    
    i = left
    j = right
    
    while i < j:
        while i < right and arr[pivot] >= arr[i] :
            i = i + 1
        
        while j > left and arr[pivot] < arr[j]:
            j = j - 1
        
        if i < j:
            arr[i], arr[j] = arr[j] , arr[i]    

    arr[j], arr[pivot] = arr[pivot], arr[j]
    return j


def partition2(arr, left, right):
    pivot = arr[right]
    i = left
    j = left
    while j <= right - 1: 
        if (arr[j] <= pivot) : 
            arr[i], arr[j] = arr[j], arr[i] 
            i = i + 1
        j = j + 1
    arr[i], arr[j] = arr[j] , arr[i]    
    return i; 


def quickSort(arr, left, right):
    if left < right :
        pivot = partition2(arr, left, right)
        quickSort(arr, left, pivot - 1)
        quickSort(arr, pivot + 1, right)


def quickSelect(arr, left, right, k):
    if left < right :
        pivot = partition(arr, left, right)
        if pivot == k:
            return arr[pivot]
        elif pivot > k:
            return quickSelect(arr, left, pivot, k)
        else:
            return quickSelect(arr, pivot + 1, right, k)
        
    
if __name__ == '__main__':
    arr = [12, 23, 1, 24, 111, 34]
    k = 4
    print(arr)
    print(quickSelect(arr, 0, len(arr) - 1, k))
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
