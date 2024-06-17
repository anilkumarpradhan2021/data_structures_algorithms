'''
Created on 19-May-2016

@author: anpradha
'''

if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 4, 4, 5, 6]
    temp = {}
    for i in range(len(arr)):
        if arr[i] in temp :
            temp[arr[i]] = temp[arr[i]] + 1
        else:
            temp[arr[i]] = 1
    
    value = list(temp.values())
    for i in range(len(value)):
        print(value[i])        
    print(temp)                         
