'''
Created on 16-Sep-2016

@author: anpradha
'''

'''

Find Median in an Unsorted Array Without Sorting it
Complexity : O(n)


This algorithm works in two steps. The partitioning step works by picking some pivot element, then rearranging the elements of the array
such that everything less than the pivot is to one side, everything greater than the pivot is to the other side, 
and the pivot is in the correct place.

Concepts  how it works.
1 . if index of pivot == kth element (pivot works exactly work as quick sort)
    break
2. if pivot index < kth element then our element is on right side so modify low  = pivot_index + 1
3. else pivot index > kth element then our element is on left side so modify high  = pivot_index - 1    


Question can be sloved :
1. This approach can be used to find the kth smallest element from an unsorted array in O(n) time
2 .This approach can be used to find the median of an unsorted array in O(n) time 
'''


def partition(low, high):
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


def select_kth_element(arr, kth):
    print(arr)
    low = 0
    high = len(arr) - 1
    while low<=high:
        pivot_index = partition(low, high)
        if pivot_index == kth:
            print(arr[pivot_index])
            break
        elif pivot_index > kth :
            high = pivot_index - 1
        else:
            low = pivot_index + 1


    

if __name__ == '__main__':
    #arr = [10, 1, 2, 23, 4, 5, 6]
    arr = [12, 3, 5, 7, 4, 26]
    select_kth_element(arr, 3)
    print(sorted(arr))
