'''
Created on 26-Apr-2021

@author: anilpradhan


Search in a sorted 2D matrix (Stored in row major order)
Difficulty Level : Medium
Last Updated : 05 Apr, 2019
Given an integer ‘K’ and a row-wise sorted 2-D Matrix i.e. the matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
The task is to find whether the integer ‘K’ is present in the matrix or not. If present then print ‘Found’ else print ‘Not found’.

Examples:

Input: mat = {
  {1,   3,  5,  7},
  {10, 11, 16, 20},
  {23, 30, 34, 50}}
  K = 3
Output: Found

Input: mat = {
  {1,   3,  5,  7},
  {10, 11, 16, 20},
  {23, 30, 34, 50}}
  K = 13
Output: Not found


Approach: The idea is to use divide and conquer approach to solve this problem.

First apply Binary Search to find the particular row i.e ‘K’ lies between the first and the last element of that row.
Then apply simple binary search on that row to find whether ‘K’ is present in that row or not.

'''

# Python 3 program to find whether a given 
# element is present in the given 2-D matrix
  
M = 3
N = 4

  
# Basic binary search to find an element 
# in a 1-D array
def binarySearch1D(arr, K):
    low = 0
    high = N - 1
    while (low <= high):
        mid = low + int((high - low) / 2)
  
        # if element found return true
        if (arr[mid] == K):
            return True
  
        # if middle less than K then skip 
        # the left part of the array 
        # else skip the right part
        if (arr[mid] < K):
            low = mid + 1
        else:
            high = mid - 1
  
    # if not found return false
    return False

  
# Function to search an element in a matrix 
# based on Divide and conquer approach
def searchMatrix(matrix, K):
    low = 0
    high = M - 1
    while (low <= high):
        mid = low + int((high - low) / 2)
  
        # if the element lies in the range
        # of this row then call
        # 1-D binary search on this row
        if (K >= matrix[mid][0] and 
            K <= matrix[mid][N - 1]):
            return binarySearch1D(matrix[mid], K)
  
        # if the element is less then the
        # starting element of that row then
        # search in upper rows else search
        # in the lower rows
        if (K < matrix[mid][0]):
            high = mid - 1
        else:
            low = mid + 1
  
    # if not found
    return False

  
# Driver code
if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    K = 3
    if (searchMatrix(matrix, K)):
        print("Found")
    else:
        print("Not found")
  
# This code is contributed by
# Shashank_Sharma
