'''
Created on 11-Nov-2019

@author: anpradha

Given an n x n square matrix, find sum of all sub-squares of size k x k
Given an n x n square matrix, find sum of all sub-squares of size k x k where k is smaller than or equal to n.
Examples :

Input:
n = 5, k = 3
arr[][] = { {1, 1, 1, 1, 1},
            {2, 2, 2, 2, 2},
            {3, 3, 3, 3, 3},
            {4, 4, 4, 4, 4},
            {5, 5, 5, 5, 5},
         };
Output:
       18  18  18
       27  27  27
       36  36  36


Input:
n = 3, k = 2
arr[][] = { {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
         };
Output:
       12  16
       24  28
       
 
 
 https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/
 
 Complexity :O(n2)      
'''

''' A O(n^2) function to find sum of all sub-squares of size k x k in a given square matrix of size n x n  
'''


def printSumTricky(mat, k , n=5): 
    
    '''k must be smaller than or equal to n else error condition'''  
    if k > n: 
        return
  
    '''
        # 1: PREPROCESSING  
        # To store sums of all strips of size k x 1  
    '''

    stripSum = [[None] * n for i in range(n)] 
  
    # Go column by column 
    for j in range(n): 
          
        ''' Calculate sum of first k x 1 rectangle in this column  '''
        Sum = 0
        for i in range(k): 
            Sum = Sum + mat[i][j]  
        stripSum[0][j] = Sum
  
        ''' Calculate sum of remaining rectangles '''
        for i in range(1, n - k + 1): 
            Sum = Sum + (mat[i + k - 1][j] - mat[i - 1][j])  
            stripSum[i][j] = Sum
        
    '''Stage 2: CALCULATE SUM of Sub-Squares using stripSum[][] '''
    for i in range(n - k + 1): 
          
        '''Calculate and prsum of first  subsquare in this row  '''
        Sum = 0
        for j in range(k): 
            Sum = Sum + stripSum[i][j]  
        print(Sum, end=" ") 
  
        ''' # Calculate sum of remaining squares in current row by removing the leftmost  strip of previous sub-square and adding a new strip '''
        for j in range(1, n - k + 1): 
            Sum = Sum + (stripSum[i][j + k - 1] - stripSum[i][j - 1])  
            print(Sum, end=" ") 
        print()    


def printArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()    
  

if __name__ == '__main__':
    # Driver Code 
    n = 5
    mat = [[1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4],
           [5, 5, 5, 5, 5]]  
    k = 3
    printSumTricky(mat, k)  
