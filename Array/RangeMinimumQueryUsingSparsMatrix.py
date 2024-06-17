'''
Created on 09-Nov-2019

@author: anpradha

We have an array arr[0 . . . n-1]. We should be able to efficiently find the minimum value from index L (query start) to R (query end) where 0 <= L <= R <= n-1. Consider a situation when there are many range queries.

Example:

Input:  arr[]   = {7, 2, 3, 0, 5, 10, 3, 12, 18};
        query[] = [0, 4], [4, 7], [7, 8]

Output: Minimum of [0, 4] is 0
        Minimum of [4, 7] is 3
        Minimum of [7, 8] is 12


This approach supports query in O(1), but preprocessing takes O(n2) time. 
Also, this approach needs O(n2) extra space which may become huge for large input arrays.


https://www.geeksforgeeks.org/range-minimum-query-for-static-array/


'''


def printArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()    
        

def rangeMinimumUsingSparshMatrix(arr , startRange , endRange):
    sparsMatrix = [["NA" for i in range(len(arr)) ] for j in range(len(arr))]
    
    ''' '''
    for i in range(len(arr)):
        sparsMatrix[i][i] = i
    
    for i in range(0, len(arr)):  
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[sparsMatrix[i][j - 1]]:
                sparsMatrix[i][j] = j 
            else:
                sparsMatrix[i][j] = sparsMatrix[i][j - 1]
    
    printArray(sparsMatrix)   
    print("Minimum in the range between {startRange} and {endRange} is : {number}" .format(endRange=endRange,startRange=startRange,number = arr[sparsMatrix[startRange][endRange]]))                  

    
if __name__ == '__main__':
    arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    print(arr)
    rangeMinimumUsingSparshMatrix(arr, 0, 4)
    rangeMinimumUsingSparshMatrix(arr, 4, 7)
