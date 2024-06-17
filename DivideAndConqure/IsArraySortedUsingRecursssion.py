'''
Created on 18-Sep-2016

@author: anpradha
'''

def issorted(arr):
    if len(arr) < 2:
        return True
    else:
        return arr[0] <= arr[1] and issorted(arr[1:])
    
    
if __name__ == '__main__':
    arr = [1, 2, 4, 56, 77, 78]
    arr2 = [11, 2, 4, 56, 77, 78]
    print(str(issorted(arr)))
    print(str(issorted(arr2)))
