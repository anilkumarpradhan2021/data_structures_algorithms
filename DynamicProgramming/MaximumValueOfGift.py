'''
Created on 04-Aug-2017

@author: anpradha

This problem is same as that of minimum path from 0,0, to  m,n  but this is for maximum , just the change the logic from min to max
'''

gift = [[1, 10, 3, 8] , [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]


def print_array(arr):
    print("Array :  ")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end="  ")
        print()    


def get_maximum_value(gift):
    rows = len(gift)
    column = len(gift[0])
    maximum = [[0 for i in range(rows)] for j in range(column)]
    
    for i in range(0, rows):
        for j in range(0, column):
            left = 0
            up = 0
            
            if i > 0:
                up = maximum[i - 1][j]
                
            if j > 0:
                left = maximum[i][j - 1]

            maximum[i][j] = max(left, up) + gift[i][j]
    print("maximum : ")
    print_array(maximum)
    print("Gift")
    print_array(gift)

    
def get_maximum_value2(gift):
    rows = len(gift)
    column = len(gift[0])
    maximum = [[0 for i in range(rows)] for j in range(column)]
 
    maximum[0][0] = gift[0][0]

    for i in range(1, len(gift)):
        maximum[0][i] = maximum[0][i - 1] + gift[0][i]
        
    for i in range(1, len(gift)):
        maximum[i][0] = maximum[i - 1][0] + gift[i][0]
                    
    for i in range(1, rows):
        for j in range(1, column):
            maximum[i][j] = max(maximum[i - 1][j], maximum[i][j - 1]) + gift[i][j]
    print("maximum : ")
    print_array(maximum)
    print("Gift")
    print_array(gift)


if __name__ == '__main__':
    get_maximum_value(gift)
    get_maximum_value2(gift)

