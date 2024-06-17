'''
Created on 20-Nov-2016

@author: anpradha

Given a cost matrix cost[][] and a position (m, n) in cost[][], 
write a function that returns cost of minimum cost path to reach (m, n) from (0, 0). 
Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination). 
You can only traverse down, right and diagonally lower cells from a given cell, 
i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.


This problem can be solved by recursion but time complexity will be O(2^n)
so here we have solved using dynamic programming 


logic is 
1. Create  a matrix of same size 
2. update the temp matrix with temp[0][0] =  a[0][0], as its the starting point
3 . then update the 1st row of the temp / solution matrix using formula as temp[0][j] = temp[0][j-1] + arr[0][j]
4. then update the 1st column of the temp /solumn matrix using the formula as temp[i][0] = temp[i-1][0] + arr[i][0]
5. the update resst of the place using the formula : temp[i][j] = arr[i][j] + min(temp[i-1][j],temp[i][j-1])


For better understanding please refer the downlaoded video / link

'''

''' 

# A Naive recursive implementation of MCP(Minimum Cost Path) problem 


# Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C] 

'''

'''
1) Optimal Substructure 
The path to reach (m, n) must be through one of the 3 cells: (m-1, n-1) or (m-1, n) or (m, n-1). 
So minimum cost to reach (m, n) can be written as “minimum of the 3 cells plus cost[m][n]”.
minCost(m, n) = min (minCost(m-1, n-1), minCost(m-1, n), minCost(m, n-1)) + cost[m][n]




'''


def minCost(cost, m, n): 
    if (n < 0 or m < 0): 
        return float("inf") 
    elif (m == 0 and n == 0): 
        return cost[m][n] 
    else: 
        return cost[m][n] + min(minCost(cost, m - 1, n),
                                minCost(cost, m, n - 1), minCost(cost, m - 1, n - 1)) 

'''
Time Complexity of the DP implementation is O(mn) 
which is much better than Naive Recursive implementation.



 '''


def minCostDP(arr):
    
    '''Create a matrix same as that of original size '''
    solution = [ [0 for x in range(len(arr))] for x in range(len(arr[0])) ]
    print("Solution before calculation")
    print_array(solution)
    
    solution[0][0] = arr[0][0]
    
    for i in range(1, len(arr)):
        solution[0][i] = solution[0][i - 1] + arr[0][i]
        
    for i in range(1, len(arr)):
        solution[i][0] = solution[i - 1][0] + arr[i][0]
        
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            solution[i][j] = arr[i][j] + min(solution[i - 1][j], solution[i][j - 1], solution[i - 1][j - 1])

    print("Solution After calculation")    
    print_array(solution)
    
    i = len(arr) - 1
    j = len(arr[0]) - 1
    print(arr[i][j], end=" - > ")
    while i > 0 and j > 0:
        if solution[i - 1][j] < solution[i][j - 1] and solution[i - 1][j] < solution[i - 1][j - 1]:
            print(arr[i - 1][j], end=" - >")
            i = i - 1
        elif solution[i][j - 1] < solution[i - 1][j] and solution[i][j - 1] < solution[i - 1][j - 1]:
            print(arr[i][j - 1], end=" - > ")
            j = j - 1         
        else:
            print(arr[i - 1][j - 1], end=" - > ")
            i = i - 1
            j = j - 1
    
    print()     
    # print(arr[0][0])

   
def print_array(arr):
    print("Array :  ")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end="  ")
        print()    


if __name__ == '__main__':
    arr = [[1, 7, 9, 2],
           [8, 6, 3, 2],
           [1, 6, 7, 8],
           [2, 9, 8, 2] 
           ]

    print_array(arr)
    minCostDP(arr)
    print(minCost(arr, len(arr) - 1, len(arr) - 1))
    
