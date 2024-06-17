'''
Created on 13-Oct-2016

@author: anpradha

Problem :
Print All Paths from Top left to bottom right in Two Dimensional Array


As we need to explore all the paths from top left cor­ner to bot­tom right cor­ner, we will either travel down OR travel right. so every time either we increase the row or column.

    Recur­sion is the key here.
    Take the rows count and col­umn counts say row­Count and col­Count respectively
    Take cur­ren­tRow =0 and cur­rent­Col­umn =0 and path =””
    Call printAll(currentRow, currentcolumn,path)
    Add array[0][0] to the path.
    Call recur­sively printAll(currentRow+1, currentcolumn,path)
    Call recur­sively printAll(currentRow, currentcolumn+1,path)
    Base Case 1: when cur­ren­tRow = rowCount-1(because array index starts with 0) , print the rest of the columns, return
    Base Case 2: when cur­rent­col­umn = colCount-1(because array index starts with 0) , print the rest of the rows, return

Please check the downloaded link for better understanding
'''

def printAllPath(matrix, currentRow, currentColumn, path):
    if currentRow == (len(matrix) - 1):
        ''' from current column to column count'''
        for i in range(currentColumn, (len(matrix[0]))):
            path = path + [matrix[currentRow][i]]
        print(path)    
        return    
            
    if currentColumn == (len(matrix[0]) - 1):
        ''' from current row to row count'''
        for i in range(currentRow, (len(matrix))):
            path = path + [matrix[i][currentColumn]]
        print(path)    
        return
        
    path = path + [matrix[currentRow][currentColumn]]
    printAllPath(matrix, currentRow + 1, currentColumn, path)
    printAllPath(matrix, currentRow, currentColumn + 1, path)
    ''' Diagonal Movement'''
    #printAllPath(matrix, currentRow + 1, currentColumn + 1, path)
    

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    printAllPath(matrix, 0, 0, [])
