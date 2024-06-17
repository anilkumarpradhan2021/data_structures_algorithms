'''
Created on 16-Nov-2019

@author: anpradha
Longest Common Subsequence

LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. 
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 


Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4


https://www.youtube.com/watch?v=NnD96abizww&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=2

Time Complexity of the above implementation is O(mn) 


'''


def logestCommonSubsequencyDP(X, Y):
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
      
    # declaring the array for storing the dp values 
    L = [[0] * (n + 1) for i in range(m + 1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(1, m + 1): 
        for j in range(1, n + 1): 
            if X[i - 1] == Y[j - 1]: 
                L[i][j] = L[i - 1][j - 1] + 1
            else: 
                L[i][j] = max(L[i - 1][j] , L[i][j - 1]) 
    
    printTheSequece(L, m, n, X)
    printBoard(L, m + 1 , n + 1)
                
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n]                 


def printBoard(board, row , col):
    for i in range(row):
        for j in range(col):
            print(board[i][j], end=" ")
        print()



''' Print is Simple Just check from backwards , Check the Video for logic simple '''
def printTheSequece(arr, m, n, X):
    i = m
    j = n
    common_seq = []
    while i > 0 and j > 0:
        if arr[i - 1][j] == arr[i][j]:
            i = i - 1
        elif arr[i][j - 1] == arr[i][j]: 
            j = j - 1
        else:
            common_seq.insert(0, X[i - 1])
            i = i - 1
            j = j - 1      

    print(common_seq)

if __name__ == '__main__':
    X = "ABCDGH"
    Y = "AEDFHR"
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(X)
    print(Y)
    print("Length of LCS is ", logestCommonSubsequencyDP(X, Y))
