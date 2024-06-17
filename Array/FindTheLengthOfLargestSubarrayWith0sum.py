'''
Created on 08-Nov-2019

@author: anpradha


Find the length of largest subarray with 0 sum

Given an array of integers, find the length of the longest subarray with sum equals to 0.

Examples :

    Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
    Output: 5
    The largest subarray with 0 sum is -2, 2, -8, 1, 7
    
    
    
'''


def findTheLengthOfLargestSubArrayhavingSumZero(arr):
    sum = 0
    maxLength = 0
    d = {}
    startIndex = 0
    endIndex = 0
    
    for i in range(len(arr)):
        sum = sum + arr[i]

        ''' This condition not required '''
        ''' this is to handle scenario where we have arr[i] is 0 , and no other '''        
        if arr[i] == 0 and maxLength == 0:
            maxLength = 1
            startIndex = i
            endIndex = i
        
        ''' this is for scenario where the sub array starts from starting of the index and end somewhewre in '''
        if sum == 0:
            maxLength = i + 1   
            endIndex = i
        
        if sum in d:
            if maxLength < i - d[sum]:
                maxLength = i - d[sum]
                
                ''' +1 because the rest of element cancel each other , this d[sum] element does not contribute anything'''
                startIndex = d[sum] + 1
                endIndex = i
        else:
            d[sum] = i    
    
    print("maxLength : " , maxLength)   
    print("Sub Array  : " , arr[startIndex:endIndex + 1]) 


if __name__ == '__main__':
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    findTheLengthOfLargestSubArrayhavingSumZero(arr)

    arr = [15, 0 , 1 , -1, 10, 23]
    findTheLengthOfLargestSubArrayhavingSumZero(arr)

    arr = [15, 0 , 1 , 1, 10, 23]
    findTheLengthOfLargestSubArrayhavingSumZero(arr)

    arr = [0 , 1 , 1, 10, 23]
    findTheLengthOfLargestSubArrayhavingSumZero(arr)
