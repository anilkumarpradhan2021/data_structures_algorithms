'''
Created on 29-Jul-2019

@author: anpradha

Smallest sum contiguous subarray


Given an array containing n integers. The problem is to find the sum of the elements of the contiguous subarray having the smallest(minimum) sum.

Examples:

Input : arr[] = {3, -4, 2, -3, -1, 7, -5}
Output : -6
Subarray is {-4, 2, -3, -1} = -6

Input : arr = {2, 6, 8, 1, 4}
Output : 1



'''

if __name__ == '__main__':
    arr = [3, -4, 2, -3, -1, 7, -5]
    #arr = [2, 6, 8, 1, 4]
    min_final = float("inf")
    min_so_far = float("inf")
    
    for i in range(len(arr)) :
        min_so_far = min(min_so_far + arr[i], arr[i])
        min_final = min(min_final, min_so_far)
    print(min_final)