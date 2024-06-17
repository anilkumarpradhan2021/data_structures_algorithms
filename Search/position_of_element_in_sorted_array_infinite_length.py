'''
Created on 15-Sep-2016

@author: anpradha
'''
'''

Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array.
If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.

Let low be pointing to 1st element (arr[0]) and high pointing to 2nd (arr[1]) element of array, Now compare key with high index element,

->if it is greater than high index element then copy high index in low index and double the high index.
->if it is smaller, then apply binary search on high and low indices found.
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

if __name__ == '__main__':
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    print(arr)
    lower_bound = 0
    upper_bound = 1
    val = arr[upper_bound]
    element_to_search  = 91
    
    while val < element_to_search :
        lower_bound = upper_bound # // store previous upper_bound
        upper_bound = upper_bound * 2 # Update the upper bound
        val = arr[upper_bound] # update the val to value at upper bound
    
    '''
    At this point we have updated lower bound and upper bound  indices, thus use binary search between them
    '''
    print(binary_search(arr, lower_bound, upper_bound, element_to_search))   
        
    
