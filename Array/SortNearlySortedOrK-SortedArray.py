'''
Created on 04-Sep-2019

@author: anpradha

Sort a nearly sorted (or K sorted) array
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Examples:

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}


The detailed process that uses Heap.
1) Create a Min Heap of size k+1 with first k+1 elements. This will take O(k) time .
2) One by one remove min element from heap, put it in result array, and add a new element to heap from remaining elements.

Removing an element and adding a new element to min heap will take Logk time. So overall complexity will be O(k) + O((n-k)*logK)
'''

from heapq import heappop, heappush, heapify 


# Given an array of size n, where every   
# element is k away from its target  
# position, sorts the array in O(nLogk) time. 
def sort_k(arr, n, k): 
    """ 
    :param arr: input array 
    :param n: length of the array 
    :param k: max distance, which every  
     element is away from its target position. 
    :return: None 
    """
    # List of first k+1 items 
    heap = arr[:k + 1] 
  
    # using heapify to convert list  
    # into heap(or min heap) 
    heapify(heap) 
  
    # "rem_elmnts_index" is index for remaining  
    # elements in arr and "target_index" is  
    # target index of for current minimum element  
    # in Min Heap "heap". 
    target_index = 0
    for rem_elmnts_index in range(k + 1, n): 
        arr[target_index] = heappop(heap) 
        heappush(heap, arr[rem_elmnts_index]) 
        target_index = target_index + 1
  
    while heap: 
        arr[target_index] = heappop(heap) 
        target_index = target_index + 1


if __name__ == '__main__':
    arr = [6, 5, 3, 2, 8, 10, 9] 
    k = 3
    sort_k(arr,k,len(arr))
    print("Sorted Array now : " , arr)
