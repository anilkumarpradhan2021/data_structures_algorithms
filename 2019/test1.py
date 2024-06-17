'''
Created on 31-Jul-2019

@author: anpradha
'''

if __name__ == '__main__':
    arr = [3 , 7  , 4, 2 , 4 , 6, 8 , 5, 9 , 3]
    arr = [8 , -4, 4, 2, 2, 6, 1, 1, 1, 1 ,1,2,3,4,5]
    n = 5
    
    j = 0 
    sum = arr[0]
    for i in range(1, n):
        j = j + i
        
        if arr[j] > arr[j + 1]:
            sum = sum + arr[j]
            print(arr[j])
        else:
            sum = sum + arr[j + 1]
            print(arr[j + 1])
            j = j + 1    
    
    print(sum)
