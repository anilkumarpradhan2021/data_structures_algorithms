'''
Created on 16-Sep-2016

@author: anpradha
'''

'''
Given an array of n distinct integers sorted in ascending order, write a function that returns a Fixed Point in the array, 
if there is any Fixed Point present in array, else returns -1. Fixed Point in an array is an index i such that arr[i] is equal to i. 
Note that integers in array can be negative.

Example :
  Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3 

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0 


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point
  
  

'''

'''
Complexity : O(n)  

(Linear Search) 

'''


def find_fixed_point(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            print("fixed point exists : " + str(i))


'''
Using binary search but without recursion 
Complexity : O(logn)

(Binary Search)

This works for unique eleements 
'''


def find_fixed_point2(arr, low, high):
    while low < high:
        mid = (low + high) // 2 
        if arr[mid] == mid :
            print("fixed point exists : " + str(mid))
            break
        elif arr[mid] > mid :
            high = mid - 1
        else:
            low = mid + 1   
    return -1 

        
def find_fixed_point_with_duplicate(arr, low, high):
    if low <= high:
        mid = (low + high) // 2 
        
        midValue = arr[mid]
        if arr[mid] == mid :
            return mid

        ''' search left'''
        leftIndex = min(mid - 1, midValue)
        left = find_fixed_point_with_duplicate(arr, low, leftIndex)
        if left >= 0:
            return left

        ''' search right'''
        rightIndex = max(mid + 1, midValue)
        right = find_fixed_point_with_duplicate(arr, rightIndex, high)
        
        return right
    else:
        return -1

    
if __name__ == '__main__':
    arr = [-10, -5, 1, 2, 7]
    arr = [-10, -5, 0, 3, 7]    
    print(find_fixed_point(arr)) 
    find_fixed_point2(arr, 0, len(arr) - 1)
    arr = [-1, -1, -1, 3, 7, 9]
    arr = [-10, -1, 3, 3, 10,
              30, 30, 50, 100]
    print(find_fixed_point_with_duplicate(arr, 0, len(arr)))
    
