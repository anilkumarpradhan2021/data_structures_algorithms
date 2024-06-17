'''
Created on 22-Oct-2019

@author: anpradha

N Queen Problem | Backtracking-3
We have discussed Knight’s tour and Rat in a Maze problems in Set 1 and Set 2 respectively. Let us discuss N Queen as another example problem that can be solved using Backtracking.
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. For example, following is a solution for 4 Queen problem.

https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

Note:
There is another solution with isSafeToPlace optimization

'''

N = 4


def printBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafeToPlace(board, row, col):
    
    ''' check for each left side row if any queen is present'''
    for col_index in range(col):
        if board[row][col_index] == 1:
            return False
        
    ''' check for diagonally left side up/upper'''
    i = row 
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i = i - 1
        j = j - 1 
    
    ''' check for diagonally left side down/lower'''
    i = row    
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1 
    
    return True    


def solveQueenUtil(board, col):
    
    ''' if col is >=N means all queen are placed '''
    if col >= N:
        return True
    
    '''  Consider this column and try placing  this queen in all rows one by one '''
    for row in range(N):
        
        ''' check for each row if we can place the queen'''
        if isSafeToPlace(board, row, col):
            
            '''Place this queen in board[row][col]'''
            board[row][col] = 1
            
            ''' recur to place rest of the queens  '''
            if solveQueenUtil(board, col + 1) == True:
                return True
            
            ''' If placing queen in board[row][col] doesn't lead to a solution, then remove queen from board[row][col] '''
            board[row][col] = 0
            
    return False        
        
                    
def solveNQueen(board):
    
    if solveQueenUtil(board, 0):
        printBoard(board)
        return True
    

if __name__ == '__main__':
    board = [[0 for i in range(N)] for j in range(N)]
    solveNQueen(board)
