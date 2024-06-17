'''
Created on 07-Sep-2016

@author: anpradha
'''

'''
Idea is select an element/index and compare with all other element , so after 1st execution , 1st element is in right 
position . so left 1st element , go for 2nd element and follow the same method .

let arr = [12, 23, 1, 24]

step-1  (i =0 , so 1st element with all other element)
execution complete , result array is :
arr = [24, 12, 1, 23]

step-2 (i = 1 , so 2nd element with all other element)
execution complete , result array is :
arr = [24, 23, 1, 12]

'''

def selection_sort(A):
    for i in range(len(A)):
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i] 
                
    
if __name__ == '__main__':
    arr = [12, 23, 1, 24, 111, 34, 1, 12, 2 , 2]
    print("Array Before Sort : " + str(arr))
    selection_sort(arr)
    print("Array after Sort : " + str(arr))
    
