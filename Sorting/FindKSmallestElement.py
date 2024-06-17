'''
Created on 29-May-2017

@author: anpradha


k largest(or smallest) elements in an array | added Min Heap method

Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.

For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.


'''


class MyClass(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.arr = [12, 23, 1, 24, 111, 34, 2]
        

'''
updated on 01/10/2019

'''

'''
    Hoare-Partition
'''


def partition(arr, low, high):
        pivot = low
        i = low
        j = high

        while i < j :
            while i < high and arr[i] <= arr[pivot]:
                i = i + 1
                
            while j > low and arr[j] > arr[pivot]:
                j = j - 1
    
            if i < j:
                ''' Swap '''
                arr[i] , arr[j] = arr[j], arr[i]
        
        arr[j] , arr[pivot] = arr[pivot], arr[j]
        return j


'''
Lomuto’s Partition Scheme

partition(arr[], lo, hi) 
    pivot = arr[hi]
    i = lo     // place for swapping
    for j := lo to hi – 1 do
        if arr[j] <= pivot then
            swap arr[i] with arr[j]
            i = i + 1
    swap arr[i] with arr[hi]
    return i



'''


def  lomutoPartition(arr, left, right):
    pivot = arr[right]
    i = left
    
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            
    arr[i], arr[right] = arr[right], arr[i]
    return i         


def findKSmallestElements(arr , position, left, right):
    if position >= left and position <= right:
        pivot = partition(arr, left, right)
        if position == pivot:
            return arr[:pivot]
        elif position < pivot:
            return findKSmallestElements(arr, position, left, pivot - 1)
        else:
            return findKSmallestElements(arr, position, pivot + 1, right)
                       


def quickSort(arr, low, high):
    
    if low < high:
        pivot = lomutoPartition(arr, low, high) 
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

        
if __name__ == "__main__":
    a = MyClass()
    arr = [11, 22, 3, 4, 35, 6, 72, 8]
    print(findKSmallestElements(arr, 5, 0, (len(arr) - 1)))
    
    arr = [1, 23, 12, 9, 30, 2, 50 ]
    print(findKSmallestElements(arr, 3, 0, (len(arr) - 1)))


    print("Before sort")
    print(arr)
    arr = [60, 61, 9, 30, 2, 50 ]
    print("After sort")
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
