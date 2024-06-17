'''
Created on 15-Sep-2016

@author: anpradha
'''



'''
Linear search for unsorted array 

'''
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 512, 56, 0, 77, 22]
    element_to_Search = 4
    for i in range(len(arr)):
        if arr[i] == element_to_Search:
            print("Found the element : Index Number : " + str(i))
