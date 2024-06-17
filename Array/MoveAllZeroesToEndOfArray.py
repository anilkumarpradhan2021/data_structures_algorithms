'''
Created on 17-Sep-2019

@author: anpradha


Move all zeroes to end of array
Given an array of random numbers, Push all the zero’s of a given array to the end of the array. 
For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0},
it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. 

The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

Example:

Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};


'''


def solution2(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count = count + 1
    
    while count < len(arr):
        arr[count] = 0
        count = count + 1
    
    print(arr)


def solution1(arr):
    pos = -1
    for i in range(len(arr)):
        
        if pos > 0:
            if arr[i] != 0 :
                arr[pos] , arr[i] = arr[i], arr[pos]
                pos = pos + 1

        if pos < 0 and arr[i] == 0 :
            pos = i
        
    print(arr)

def sol3(arr):
    i=0
    j = len(arr) -1 
    while i<j:
        while arr[i] != 0:
            i = i +1
        while arr[j] == 0:
            j = j -1
        if i < j:
            arr[i], arr[j] = arr[j],arr[i]
    print(arr)
        
if __name__ == '__main__':
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    #arr = [1, 2, 0, 0, 0, 3, 6]
    #arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
    #solution2(arr)
    sol3(arr)
