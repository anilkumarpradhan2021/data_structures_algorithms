'''
Created on 23-Nov-2019

@author: anpradha

Search in a row wise and column wise sorted matrix
Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. The designed algorithm should have linear time complexity.
Example :

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output : Found at (2, 1)

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output : Element not found


O(n)
'''


def search(mat, size, element):
    row = 0
    col = size - 1
    while row <= size - 1 and col >= 0:
        if mat[row][col] == element:
            print("element Found at ", row, ", ", col) 
            return 1
        elif  mat[row][col] > element:
            col = col - 1
        else:
            row = row + 1
    
    print("Not found")               


if __name__ == '__main__':
    mat = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] 
        ] 
    search(mat, 4, 29) 
    search(mat, 4, 400) 
