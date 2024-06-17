'''
Created on 17-Sep-2016

@author: anpradha
'''

if __name__ == '__main__':
    a = [(1, 2), (3, 4), (5, 6)]
    b = [[1, 2], [3, 4], [5, 6]]
    c = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    
    for i , j  in a:
        print(i, j)

    print("****************")
    for i , j  in b:
        print(i, j)

    print("****************")
    for i , j  in [(11, 21), (31, 41)]:
        print(i, j)

    print("****************")
    for i , j , k  in c:
        print(i, j, k)
