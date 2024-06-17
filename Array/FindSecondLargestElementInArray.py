'''
Created on 28-Aug-2019

@author: anpradha

Find Second largest element in an array
Given an array of integers, our task is to write a program that efficiently finds the second largest element present in the array.

Example:

Input : arr[] = {12, 35, 1, 10, 34, 1}
Output : The second largest element is 34.

Input : arr[] = {10, 5, 10}
Output : The second largest element is 5.

Input : arr[] = {10, 10, 10}
Output : The second largest does not exist.


'''


def secondLargest(arr):
    first_largest = float("-inf")
    second_largest = float("-inf")
    
    for i in range(len(arr)):
        if arr[i] > first_largest:
            second_largest = first_largest
            first_largest = arr[i]
        else:    
            second_largest = max(second_largest, arr[i])
    
    print("Second largest element is : " , second_largest)

def secondLargest2(arr):
    first_largest = float("-inf")
    second_largest = float("-inf")
    
    for i in range(len(arr)):
        if arr[i] > first_largest:
            second_largest = first_largest
            first_largest = arr[i]
        if arr[i] > second_largest and arr[i] < first_largest:
            second_largest = arr[i]
    
    print("Second largest element is : " , second_largest)

               
if __name__ == '__main__':
    arr = [12, 35, 1, 10, 34, 1]
    arr = [10, 5, 10]
    arr = [21, 20, 15, 30]
    secondLargest(arr)
    secondLargest2(arr)
    
