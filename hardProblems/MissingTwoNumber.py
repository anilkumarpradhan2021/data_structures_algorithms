'''
Created on 29-Oct-2019

@author: anpradha

You are given an array with all the numbers from 1 to N appearing exactly once,
except for one number that is missing. How can you find the missing number in O(N) time and
0( 1) space? What if there were two numbers missing?

https://www.geeksforgeeks.org/find-two-missing-numbers-set-2-xor-based-solution/




'''


def findTwoMissingNumber(arr, N):
    result = 0
    
    ''' XOR all element in arr'''
    for i in range(len(arr)):
        result = result ^ arr[i]
    
    ''' XOR all element in from 1 to N'''
    for i in range(1, N + 1):
        result = result ^ i
        
    print("missing 2 number xor : " , result)    
    
    ''' find the last set bit'''
    
    lastSetBit = result & (result - 1)
    
    ''' xor all element form 1 to N whose last set bit is lastSetBit'''
    num1 = 0
    num2 = 0
    for i in range(1, N + 1):
        if i & lastSetBit > 0:
            num1 = num1 ^ i
        else:
            num2 = num2 ^ i
    
    ''' xor all element XOR all element in arr  whose last set bit is lastSetBit'''
    for i in range(len(arr)):
        if arr[i] & lastSetBit > 0:
            num1 = num1 ^ arr[i]
        else:
            num2 = num2 ^ arr[i]
    
    print(num1, num2)    


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 7]
    findTwoMissingNumber(arr, 7)
