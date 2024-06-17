'''
Created on 03-Aug-2019

@author: anpradha
'''

def print_array(arr):
    #  X Represent Number of rows
    for x in range(len(arr)):
        # Y represent Number of Column
        for y in range(len(arr[x])):
            # print(" x : " + str(x) + " y : " + str(y) , end= " ")
            print(arr[x][y] , end=" ")
        print()    

if __name__ == '__main__':
    string1 = "tutorialhorizon"
    string2 = "dynamictutorialProgramming"

    string1 = "abcdef"
    string2 = "cabc"
    
    mat = [[0 for x in string1] for y in string2]
   
    max1 = mat[0][0]
    
    for i in range(0, len(string2)):
        for j in range(0, len(string1)):
            if string2[i] == string1[j]:
                mat[i][j] = mat[i - 1][j - 1] + 1
                max1 = max(max1, mat[i][j]) 
        
    print(max1)
    print_array(mat)