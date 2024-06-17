'''
Created on 03-Oct-2019

@author: anpradha

Sort an array in wave form /\_/\_/\

Given an unsorted array of integers, sort the array into a wave like array. An array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

Examples:

 Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
 Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                 {20, 5, 10, 2, 80, 6, 100, 3} OR
                 any other array that is in wave form

 Input:  arr[] = {20, 10, 8, 6, 4, 2}
 Output: arr[] = {20, 8, 10, 4, 6, 2} OR
                 {10, 8, 20, 2, 6, 4} OR
                 any other array that is in wave form

 Input:  arr[] = {2, 4, 6, 8, 10, 20}
 Output: arr[] = {4, 2, 8, 6, 20, 10} OR
                 any other array that is in wave form

 Input:  arr[] = {3, 6, 5, 10, 7, 20}
 Output: arr[] = {6, 3, 10, 5, 20, 7} OR
                 any other array that is in wave form


logic:
    we need to just take care of 0 ,2, 4, 6 ,... element means even placed element
    so 
    if arr[i] < arr[i-1] 
        swap
    if  arr[i] < arr[i+1]
        swap
        
        
                    i(High)
Easy Formula           /\
            (low)i-1 /   \ i+1 (low)


This algorithm takes O ( n) time.

'''


def waveForm(arr):
    print("Original array")
    print(arr)
    for i in range(0, len(arr), 2):
        
        if i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

        if i < len(arr) - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    print("Array in Wave form")
    print(arr)        
    
    
if __name__ == '__main__':
    arr = [3, 6, 5, 10, 7, 20]
    waveForm(arr)
    arr = [2, 4, 6, 8, 10]
    waveForm(arr)
