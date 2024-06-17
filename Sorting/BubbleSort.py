'''
Created on 07-Sep-2016

@author: anpradha
'''


'''
Bubble sort algorithm starts by comparing the first two elements of an array and swapping if necessary, i.e., 
if you want to sort the elements of array in ascending order and if the first element is greater than second then,
 you need to swap the elements but, if the first element is smaller than second, you mustn't swap the element. 
 Then, again second and third elements are compared and swapped if it is necessary and this process go on until 
 last and second last element is compared and swapped. This completes the first step of bubble sort.

If there are n elements to be sorted then, the process mentioned above should be repeated n-1 times to get required
 result. But, for better performance, in second step, last and second last elements are not compared becuase,
  the proper element is automatically placed at last after first step. Similarly, in third step, 
  last and second last and second last and third last elements are not compared and so on.
'''
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                '''
                swap
                '''
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                
if __name__ == '__main__':
    arr = [12, 23, 1, 24, 111, 34, 1, 12, 2 , 222]
    print("Array Before Sort : " + str(arr))
    bubble_sort(arr)
    print("Array Afterb bubble Sort : " + str(arr))
    
