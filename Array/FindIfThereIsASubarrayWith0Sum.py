'''
Created on 23-Sep-2019

@author: anpradha

Find if there is a subarray with 0 sum
Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.
Examples :

Input: {4, 2, -3, 1, 6}
Output: true 
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true 
There is a subarray with zero sum from index 2 to 2.

Input: {-3, 2, 3, 1, 6}
Output: false
There is no subarray with zero sum.

Example :

arr[] = {1, 4, -2, -2, 5, -4, 3}

If we consider all prefix sums, we can
notice that there is a subarray with 0
sum when :
1) Either a prefix sum repeats or
2) Or prefix sum becomes 0.

Array :
1, 4, -2, -2, 5, -4, 3
Prefix sums for above array are:
1, 5,  3,  1, 6,  2,  5

Since prefix sum 1 repeats, we have a subarray
with 0 sum. 


'''


def isThereIsSubArrayWithSUmZero(arr):
    sum = 0
    d = {}
    for i in range(len(arr)):
        sum = sum + arr[i]
        
        if sum == 0 or sum in d:
            return True
        else:
            d[sum] = sum
    return False    




if __name__ == '__main__':
    arr = [4, 2, -3, 1, 6]
    #arr = [-3, 2, 3, 1, 6]
    #arr = [4, 2, 0, 1, 6]
    print(isThereIsSubArrayWithSUmZero(arr))
