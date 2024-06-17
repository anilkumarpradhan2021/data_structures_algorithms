'''
Created on 13-Oct-2016

@author: anpradha

Complexity :O(n log n)



'''

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):

    '''create temp arrays and Copy data to temp arrays L[] and R[]'''
    L = [arr[k] for k in range(l, m + 1)]  # l to mid 
    R = [arr[k] for k in range(m + 1, r + 1)]  # mid +1 to r 
 
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
 
    while i < len(L) and L[i] < 0:
        arr[k] = L[i]
        i += 1
        k += 1
   
    while j < len(R) and R[j] < 0:
        arr[k] = R[j]
        j += 1
        k += 1
    # Copy the remaining elements of L[], if there
    # are any
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)    



if __name__ == '__main__':
    arr = [1, -2, 3, -4, 5 , -6, 7, -8, 9, -10 ]
    print("Array Before Sort : " + str(arr))
    mergeSort(arr, 0, len(arr) - 1)
    print("Array after Sort : " + str(arr))
