'''
Created on 07-Nov-2019

@author: anpradha

Maximum size square sub-matrix with all 1s
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

For example, consider the below binary matrix.
maximum-size-square-sub-matrix-with-all-1s



https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/

1) Construct a sum matrix S[R][C] for the given M[R][C].
     a)    Copy first row and first columns as it is from M[][] to S[][]
     b)    For other entries, use following expressions to construct S[][]
         If M[i][j] is 1 then
            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
         Else /*If M[i][j] is 0*/
            S[i][j] = 0
2) Find the maximum entry in S[R][C]
3) Using the value and coordinates of maximum entry in S[i], print 
   sub-matrix of M[][]
   
   
   

'''


def printArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()    


def printMaxSubSquare(M):
    
    '''create a AUX matrix exactly like M but with all entry 0'''
    Row = len(M)  # no. of rows in M[][] 
    Col = len(M[0])  # no. of columns in M[][] 
  
    S = [[0 for k in range(Col)] for l in range(Row)] 
    
    for i in range(Col):
        S[0][i] = M[0][i]
    
    for i in range(Row):
        S[i][0] = M[i][0]

    for i in range(Row):
        for j in range(Col):
            if M[i][j] == 1:
                S[i][j] = min(S[i - 1][j], S[i - 1][j - 1] , S[i][j - 1]) + 1
            else:
                S[i][j] = 0    

    printArray(S)
    
    max_i = 0
    max_j = 0
    max_entry = 0
    for i in range(Row):
        for j in range(Col):
            if S[i][j] > max_entry:
                max_entry = S[i][j]
                max_i = i
                max_j = j
    print("Maximum Sqaure Matrix possible , " , max_entry)
                

if __name__ == '__main__':
    M = [
            [0, 1, 1, 0, 1],
            [1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
    
    printArray(M)
    print("---------------")
    printMaxSubSquare(M)
