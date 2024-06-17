'''
Created on 13-Oct-2019

@author: anpradha


Median of two sorted arrays of different sizes

This is an extension of median of two sorted arrays of equal size problem. Here we handle arrays of unequal size also.

Method 1: (Linear and Simpler Approach)
Here we need to find the median of the two sorted arrays of different sizes so we keep two variables to point to the arrays and one used to count the no of elements read. 
We used a simple Merge based O(n) solution just we are not merging the array instead we are keeping track of the last element read till we reach the median
There are two cases :
Case 1: m+n is odd
Then we will find a clear median at (m+n)/2 index in the array obtained after merging both the arrays so we just traverse both the arrays 
and keep the last value in m1 after the loop, m1 will contain the value of the median
Case 2: m+n is even
Median will be average of elements at index ((m+n)/2 – 1) and (m+n)/2 in the array obtained after merging both the arrays 
so we need to keep track of not only the last element but also the second last element (m2 is used for this) so we traverse both the arrays 
and keep the last value in m1 and second last value in m2 after the loop, (m1+m2)/2 will contain the value of the median.


Complexity: O(n)


This very simple as we have merge sort 

'''


def median(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    m1 = -1
    m2 = -1
    arr1_index = 0
    arr2_index = 0
    median_index = 0
    max_median_position = (arr1_len + arr2_len) // 2
    
    # for even case (means len(arr1) + len(arr2) is even , then find middle 2 element and avg it 
    if (arr1_len + arr2_len) % 2 == 0:
        while arr1_index < arr1_len and arr2_index < arr2_len and median_index <= max_median_position:
            
            if arr1[arr1_index] < arr2[arr2_index]:
                m1 = m2
                m2 = arr1[arr1_index]
                arr1_index = arr1_index + 1
            
            elif arr2[arr2_index] < arr1[arr1_index]:
                m1 = m2
                m2 = arr2[arr2_index]
                arr2_index = arr2_index + 1
                
            median_index = median_index + 1
        
        while arr1_index < arr1_len and median_index <= max_median_position:
            m1 = m2
            m2 = arr1[arr1_index]
            arr1_index = arr1_index + 1
            median_index = median_index + 1

        while arr2_index < arr2_len and median_index <= max_median_position:
            m1 = m2
            m2 = arr2[arr2_index]
            arr2_index = arr2_index + 1
            median_index = median_index + 1
            
        print((m1 + m2) // 2)
        
    else:
        while arr1_index < arr1_len and arr2_index < arr2_len and median_index <= max_median_position:
            if arr1[arr1_index] < arr2[arr2_index]:
                m2 = arr1[arr1_index]
                arr1_index = arr1_index + 1
            
            elif arr2[arr2_index] < arr1[arr1_index]:
                m2 = arr2[arr2_index]
                arr2_index = arr2_index + 1
                
            median_index = median_index + 1
        
        while arr1_index < arr1_len and median_index <= max_median_position:
            m2 = arr1[arr1_index]
            arr1_index = arr1_index + 1
            median_index = median_index + 1

        while arr2_index < arr2_len and median_index <= max_median_position:
            m2 = arr2[arr2_index]
            arr2_index = arr2_index + 1
            median_index = median_index + 1
        
        print(m2)


if __name__ == '__main__':
    arr1 = [900, 1000]
    arr2 = [5, 8, 10, 20]
    median(arr1, arr2)
