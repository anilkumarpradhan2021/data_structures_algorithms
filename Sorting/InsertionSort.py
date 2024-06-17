'''
Created on 07-Sep-2016

@author: anpradha
'''


'''
Idea is insert an element into its proper position like sorting "deck of card". so how to do it ?
It starting from the second position and backtracks , find the exact spot, where the current number should belong 
and put it there. But along with the backtracking, it actually swaps each intermediate element, so in the end of one main cycle
 the whole sequence has a change.
 
 
  The main idea of insertion sort is
• Start by considering the first two elements of the array data. If found out of order, swap them
• Consider the third element; insert it into the proper position among the first three elements.
• Consider the fourth element; insert it into the proper position among the first four elements.
• … … 

e.g 
Array = [12, 3, 1, 5, 8]
when  i= 1 i.e arr[1] = 3 ,need to find the correct place for 3 [12,3].so in step-1 [3,12] ,so final result is [3, 12, 1, 5, 8]
when  i= 2 i.e arr[2] = 1 ,need to find the correct place for 1 [3,12,1].so in step-2 [3,1,12],[1,3,12] final result is [1, 3, 12, 5, 8]
when  i= 3 i.e arr[3] = 5 ,need to find the correct place for 5 [1,3,12,5].so in step-3 [1,3,5,12] so final result is [1, 3, 5, 12, 8]
when  i= 3 i.e arr[4] = 8 ,need to find the correct place for 5 [1,3,5,12,8].so in step-4 , [1,3,5,8,12] so final result is [1, 3, 5, 8, 12]
 
Worst Case: O(n^2)
Average Case: O(n^2)
Best Case: O(n)


'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        ''' fix one element and check all element before it , if greater than fix element, swap it '''
        index_val = arr[i]
        j = i
        while(j > 0 and arr[j - 1] > index_val):
            ''' swap '''
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1
        ''' NO more element > fix element , so we found the correct position for fix element.'''    
        arr[j] = index_val
                    
def try1(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] > arr[j-1]:
                print("Hi")
                arr[j], arr[j-1] = arr[j-1] ,arr[j]
                        
if __name__ == '__main__':
    arr = [12, 3, 1, 5, 8]
    print("Array Before Sort : " + str(arr))
    try1(arr)
    #insertion_sort(arr)
    print("Array after Sort : " + str(arr))
