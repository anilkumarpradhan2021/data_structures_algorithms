'''
Created on 28-Aug-2019

@author: anpradha

Largest sum contiguous increasing subarray
Given an array of n positive distinct integers. The problem is to find the largest sum of contiguous increasing subarray in O(n) time complexity.

Examples :

Input : arr[] = {2, 1, 4, 7, 3, 6}
Output : 12
Contiguous Increasing subarray {1, 4, 7} = 12

Input : arr[] = {38, 7, 8, 10, 12}
Output : 38



'''


def solution1(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    i = 0 
    while i < len(arr) - 1:
        if arr[i + 1] > arr[i]:
            current_sum = current_sum + arr[i + 1]
        else:
            # max_sum = max(max_sum, current_sum)
            current_sum = arr[i + 1]
        max_sum = max(max_sum, current_sum)

        i = i + 1
    print(max_sum)


def solution2(arr):
    max_sum = float("-inf")
    
    i = 0
    while i < len(arr):
        
        current_sum = arr[i]
        
        while i + 1 < len(arr) and  arr[i + 1] > arr[i]:
            current_sum = current_sum + arr[i + 1]
            i = i + 1

        max_sum = max(max_sum, current_sum)
        
        i = i + 1

    print(max_sum)        


''' working solution'''
def solution3(arr):
    max_sum = float("-inf")
    for i in range(len(arr)):
        current_sum = arr[i]
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            current_sum = current_sum + arr[i + 1]
            i = i + 1
        max_sum = max(max_sum, current_sum)

    print(max_sum)        


if __name__ == '__main__':
    #arr = [2, 1, 4, 7, 3, 6]
    arr = [38, 7, 8, 10, 12]
    solution1(arr)
    solution2(arr)
    solution3(arr)
    
