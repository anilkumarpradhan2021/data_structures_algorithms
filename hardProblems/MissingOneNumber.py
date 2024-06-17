'''
Created on 29-Oct-2019

@author: anpradha

You are given an array with all the numbers from 1 to N appearing exactly once,
except for one number that is missing. How can you find the missing number in O(N) time and
0( 1) space?


'''


def findMissingNumber(arr, N):
    result = 0
    
    ''' XOR all element in arr'''
    for i in range(len(arr)):
        result = result ^ arr[i]
    
    ''' XOR all element in from 1 to N'''
    for i in range(1, N + 1):
        result = result ^ i
        
    print("missing number is : " , result)    
        

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 6, 7]
    findMissingNumber(arr, 7)
    
