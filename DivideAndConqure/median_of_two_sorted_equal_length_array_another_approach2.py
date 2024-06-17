'''
Created on 21-Sep-2016

@author: anpradha



Method 2 (By comparing the medians of two arrays)
This method works by first getting medians of the two sorted arrays and then comparing them.

Let ar1 and ar2 be the input arrays.

Algorithm:

1) Calculate the medians m1 and m2 of the input arrays ar1[] 
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one 
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one    
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays 
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get 
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
    
    Time Complexity: O(logn)
Algorithmic Paradigm: Divide and Conquer

'''

''' Function to get median of a sorted array  '''


def median_of_sorted_array(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2] + arr[(n // 2 - 1)]) // 2
    else:
        return arr[n // 2]

        
''' This function returns median of ar1[] and ar2[].
   Assumptions in this function:
   Both ar1[] and ar2[] are sorted arrays
   Both have n elements
   
   '''


def median_of_two_sorted_equal_length_array2(arr1, arr2, n):
    
    if n == 0 :
        return -1
    if n == 1:
        return (arr1[0] + arr2[0]) / 2
    if n == 2 :
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) // 2
    
    m1 = median_of_sorted_array(arr1)
    m2 = median_of_sorted_array(arr2)
    
    '''If medians are equal then return either m1 or m2 '''
    if m1 == m2:
        return m1
    
    ''' if m1 > m2 then median must exist in ar1[....m1] and
        ar2[m2...]  '''
    if m1 > m2:
        if n % 2 == 0:
            return median_of_two_sorted_equal_length_array2(arr1[:n // 2 + 1], arr2[n // 2:], n // 2)
        return median_of_two_sorted_equal_length_array2(arr1[:n // 2 + 1], arr2[n // 2:], n // 2 + 1)

    ''' if m2 > m1 then median must exist in ar1[m1....] and
        ar2[....m2]'''
    if m2 > m1:
        if n % 2 == 0:
            return median_of_two_sorted_equal_length_array2(arr1[n // 2:], arr2[:n // 2 + 1], n // 2)
        return median_of_two_sorted_equal_length_array2(arr1[n // 2:], arr2[:n // 2 + 1], n // 2 + 1)

                
if __name__ == '__main__':
    arr1 = [1, 12, 15, 26, 38]
    arr2 = [2, 13, 17, 30, 45]
    arr1 = [1, 10 , 20]
    arr2 = [20, 30, 40]
    #arr1 = [1, 10]
    #arr2 = [20, 30]
    print(median_of_two_sorted_equal_length_array2(arr1, arr2, len(arr1)))
