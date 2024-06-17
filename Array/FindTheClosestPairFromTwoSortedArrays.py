'''
Created on 24-Sep-2019

@author: anpradha

Find the closest pair from two sorted arrays
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.
We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x, we need to find the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] – x) is minimum.

Example:

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40


''' 


def  findTheClosestPairFromTwoSortedArrays(arr1, arr2, number):
    left = 0 
    right = len(arr2) - 1
    diff = float("inf")
    element_from_arr1 = arr1[0]
    element_from_arr2 = arr2[0]
    
    while left < len(arr1) and right >= 0:
        
        # update the diff
        if abs(arr1[left] + arr2[right] - number) < diff:
            element_from_arr1 = arr1[left]
            element_from_arr2 = arr2[right]
            
            diff = abs(arr1[left] + arr2[right] - number)
            
        
        if arr1[left] + arr2[right] > number:
            right = right - 1
        else:
            left = left + 1
    
    print("diff : " , diff)
    print("element_from_arr1 : " , element_from_arr1 , "element_from_arr2 : " , element_from_arr2)    
    
    
if __name__ == '__main__':
    arr1 = [1, 4, 5, 7]
    arr2 = [10, 20, 30, 40]
    number = 32
    number = 50
    findTheClosestPairFromTwoSortedArrays(arr1, arr2, number)
     
