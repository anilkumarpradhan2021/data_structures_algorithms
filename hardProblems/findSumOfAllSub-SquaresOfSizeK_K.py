'''
Created on 06-Nov-2019

@author: anpradha

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


Time complexity of above solution is O(k2n2)

              
'''


def sumOfSubSquare(matrix, row, col, k):
    sum = 0
    for i in range(row, row + k):
        for j in range(col, col + k):
            sum = sum + matrix[i][j]
    
    print(sum ,end = " ")        
    
    
def findTheSumOfAllSubSquareK(matrix, k):
    for i in range(len(matrix) - k + 1):
        for j in range(len(matrix) - k + 1):
            sumOfSubSquare(matrix, i, j, k)
        print()    

            
if __name__ == '__main__':
    arr = [ [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5],
         ]
    k = 3
         
    findTheSumOfAllSubSquareK(arr, k)
