'''
Created on 13-Oct-2016

@author: anpradha

Problem :

Count all possible paths from top left to bottom right of a mXn matrix

The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell 
you can either move only to right or down


Time Complexity Recursion :
The time complexity of above recursive solution is exponential.

'''
def countAllPathUsingRecursion(rowNumber, columnNumber):
    ''' Base case '''

    if rowNumber == 1 or columnNumber == 1:
        return 1
    else:
        
        '''If diagonal movements are allowed then the last addition is required'''
        return countAllPathUsingRecursion(rowNumber - 1, columnNumber) + countAllPathUsingRecursion(rowNumber, columnNumber - 1) + countAllPathUsingRecursion(rowNumber - 1, columnNumber - 1) 



'''Time complexity of the above dynamic programming solution is O(mn). '''

def countAllPathUsingDynamicProgramming(rowNumber, columnNumber):
    ''' Create a 2 dimentional Array'''
    temp = [[[] for _ in range(columnNumber)] for _ in range(rowNumber)]
    
    '''Count of paths to reach any cell in first column is 1'''
    for i in range(len(temp)):
        temp[i][0] = 1

    '''Count of paths to reach any cell in first row is 1 '''
    for i in range(len(temp[0])):
        temp[0][i] = 1

    '''Calculate count of paths for other cells in bottom-up manner using the recursive solution'''
    for i in range(1, len(temp)):
        for j in range(1, len(temp[0])):
            ''' 1st portion is for diagonal movement'''
            temp[i][j] = temp[i - 1][j - 1] + temp[i][j - 1] + temp[i - 1][j] 
    
    ''' Just for printing the temp array'''        
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            print(temp[i][j], end=" ")
        print()    
        
    print(temp[rowNumber - 1][columnNumber - 1])    

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(countAllPathUsingRecursion(3, 3))
    countAllPathUsingDynamicProgramming(3, 3)
