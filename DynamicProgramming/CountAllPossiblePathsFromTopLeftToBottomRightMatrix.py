'''
Created on 17-Nov-2019

@author: anpradha


Count all possible paths from top left to bottom right of a mXn matrix

The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down

Examples :

Input :  m = 2, n = 2;
Output : 2
There are two paths
(0, 0) -> (0, 1) -> (1, 1)
(0, 0) -> (1, 0) -> (1, 1)

Input :  m = 2, n = 3;
Output : 3
There are three paths
(0, 0) -> (0, 1) -> (0, 2) -> (1, 2)
(0, 0) -> (0, 1) -> (1, 1) -> (1, 2)
(0, 0) -> (1, 0) -> (1, 1) -> (1, 2)



'''

# Python program to count all possible paths  
# from top left to bottom right 

  
# Returns count of possible paths to reach cell  
# at row number m and column number n from the  
# topmost leftmost cell (cell at 1, 1) 
def numberOfPaths(m, n): 
    # Create a 2D table to store 
    # results of subproblems 
    count = [[0 for x in range(m)] for y in range(n)] 
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for i in range(n): 
        count[i][0] = 1; 
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for j in range(m): 
        count[0][j] = 1; 
    
    # Calculate count of paths for other 
    # cells in bottom-up  
    # manner using the recursive solution 
    for i in range(1, n): 
        for j in range(1, m):              
            count[i][j] = count[i - 1][j] + count[i][j - 1] 
    
    printBoard(count, n , m)        
    return count[n - 1][m - 1] 

def printBoard(board, row , col):
    for i in range(row):
        for j in range(col):
            print(board[i][j], end=" ")
        print()


if __name__ == '__main__':
    m = 4
    n = 5
    print(numberOfPaths(m, n)) 
