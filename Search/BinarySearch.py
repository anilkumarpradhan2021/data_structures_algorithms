'''
Created on 15-Sep-2016

@author: anpradha
'''

'''
Binary Search for Sorted list and length of array is known.

'''


def binary_search(arr, low, high, element_to_Search):
    if low <= high:
        mid = (low + high) // 2 
        if arr[mid] == element_to_Search:
            return mid
        elif arr[mid] < element_to_Search:
            return binary_search(arr, mid + 1, high, element_to_Search)
        else:
            return binary_search(arr, low , mid - 1, element_to_Search)
    else:
        return -1    


def binary_search2(arr, low, high, element_to_Search):
    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == element_to_Search:
            return mid
        elif arr[mid] < element_to_Search:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return -1    

        
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 12, 15, 67, 111, 1111]
    element_to_Search = 1111
    print(binary_search(arr, 0, len(arr) - 1, element_to_Search))
    print(binary_search2(arr, 0, len(arr) - 1, element_to_Search))

