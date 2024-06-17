'''
Created on 18-Nov-2019

@author: anpradha

Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Examples:

Input: arr[]   = {2, 0, 2}
Output: 2
Structure is like below
| |
|_|
We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 0, 2, 0, 4}
Output: 10
Structure is like below
     |
|    |
|  | |
|__|_| 
We can trap "3*2 units" of water between 3 an 2,
"1 unit" on top of bar 2 and "3 units" between 2 
and 4.  See below diagram also.

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
       | 
   |   || |
_|_||_||||||
Trap "1 unit" between first 1 and 2, "4 units" between
first 2 and 3 and "1 unit" between second last 1 and last 2 

https://www.geeksforgeeks.org/trapping-rain-water/



'''

'''Time complexity of this solution is O(n2).
water trapped at any element = min( max_left, max_right) – arr[i] 
'''


def maxWater(arr):
    result = 0 
    for i in range(1, len(arr)):
        '''Find the maximum element on its left '''
        left = max(arr[:i + 1])

        '''Find the maximum element on its right '''
        right = max(arr[i:])
        
        ''' update maximum water is '''
        result = result + min(left, right) - arr[i]
    print("Max water can be stored : ", result)    


'''
Time Complexity: O(n)
Auxiliary Space: O(1)
'''


def findWater(arr):
    result = 0 
    leftMax = 0
    rightMax = 0 
    left = 0
    right = len(arr) - 1
    
    while left <= right :
        
        ''' looking for min( max_left, max_right) so left is small here so in '''
        if arr[left] < arr[right]:
            ''' if current is > leftMax then update left max and we can't hold any water '''
            if arr[left] > leftMax:
                leftMax = arr[left]
            else:
                '''as current is less than leftMax so water on curr element = leftMax - curr '''
                result = result + leftMax - arr[left]    
            
            left = left + 1
        else:

            ''' if current is > rightMax then update left max and we can't hold any water '''
            if arr[right] > rightMax:
                ''' update right max'''
                rightMax = max(rightMax, arr[right])
            else:
                result = result + rightMax - arr[right]                        
            right = right - 1

    print("Max water can be stored O(n) : ", result)    
        
    
if __name__ == '__main__':
    arr = [3, 0, 0, 2, 0, 4]
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    maxWater(arr)
    findWater(arr)
