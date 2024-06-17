'''
Created on 10-Sep-2016

@author: anpradha
'''

'''
The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. 
Radix sort uses counting sort as a subroutine to sort.

The Radix Sort Algorithm
1) Do following for each digit i where i varies from least significant digit to the most significant digit.
………….a) Sort input array using counting sort (or any stable sort) according to the i’th digit.

Example:
Original, unsorted list:

    170, 45, 75, 90, 802, 24, 2, 66

Sorting by least significant digit (1s place) gives: [*Notice that we keep 802 before 2, because 802 occurred before 2 in the original list, and similarly for pairs 170 & 90 and 45 & 75.]

    170, 90, 802, 2, 24, 45, 75, 66

Sorting by next digit (10s place) gives: [*Notice that 802 again comes before 2 as 802 comes before 2 in the previous list.]

    802, 2, 24, 45, 66, 170, 75, 90

Sorting by most significant digit (100s place) gives:

    2, 24, 45, 66, 75, 90, 170, 802 
    
Complexity : O(n)

***************************** IGNORE BELOW If YOU WANT ONLY RADIX SORT *******************************



Radix Sort takes O(d*(n+b)) time 
where b is the base
      d is number of digit in a number 
      n total number of elements in the given set
      
      e.g 
      let b = 10 (decimal number )
      let k is the maximum possible value 
      so need to find d which is number of digit in K , we can find in logb(k)  time (like finding the least to most significant digit )
      So overall time complexity is O((n+b) * logb(k)) 
      Which looks more than the time complexity of comparison based sorting algorithms for a large k. 
      Let us first limit k. Let k <= n^c where c is a constant. 
      e.g for n between 1 to 9 and c=2 , 1,2,4...81 
      so  k =81 and d = 2 (number of digit)
      O((n+b) * logb(k)) = complexity becomes O(nLogb(n)) (still doesn’t beat comparison based sorting algorithms)
      What if we make value of b larger?. What should be the value of b to make the time complexity linear? 
      If we set b as n, we get the time complexity as O(n).
      
      e.g  O(nLogb(n)) = O(n) , when b = n 
      
      so O(d*(n+b)) = O(logbk*(n+b)) = O(logbk(n)) = O(n)
      
      So we can sort an array of integers with range from 1 to n^c in O(n) 
      If we set b as n, the value of O(logb(n)) becomes O(1) and overall time complexity becomes O(n). 
      b = base
      n = number of size
      
      
      One more question , application for radix sort
      
      Q: Sort n numbers in range from 0 to n^2 – 1 in linear time.
      Given an array of numbers of size n. It is also given that the array elements are in range from 0 to n2 – 1. Sort in O(n)
      Examples:
        e.g -1
        Since there are 5 elements, the elements can be from 0 to 24.
        Input: arr[] = {0, 23, 14, 12, 9}
        here n = 5 
        
        
        e.g -2
        Since there are 3 elements, the elements can be from 0 to 8.
        Input: arr[] = {7, 0, 2}
        here n = 3 
        
        to make it linear 
        number_of_element = k = logb(n)
        
        for n^1 , maxiumum_number_element = 1 , k = logb(n^1) , as b=n so k =1 
        for n^2 , maxiumum_number_of_base_element = 2  k = logb(n^2) , as b=n so k =2 
        for n^3 , maxiumum_number_of_base_element = 3  k = logb(n^3) , as b=n so k =3 
    
'''

def count_sort_for_radix(arr, exp):
    
    ''' As maximum Number of differnt number could be 0 - 9 so take array of size 10 '''
    '''initialize count array as 0'''
    
    ''' Assuming its a decimal number '''
    count = [0 for x in range(10)]  
    size = len(arr)
    
    '''initialize result array as 0'''
    result = [0 for x in range(size + 1)]
    
    ''' FIll count depending on arr value '''
    for i in range(len(arr)):
        index = arr[i] // exp
        count[index % 10 ] = count[index % 10 ] + 1
        
    # print("count : " + str(count))    
        
    ''' Calculate count value '''
    for i in range(1, len(count)):
        count[i] = count[i] + count[i - 1]
        
    # print("Updated count : " + str(count))    

    ''' Update result'''
    i = size - 1
    while i >= 0:
        index = arr[i] // exp
        result[count[index % 10]] = arr[i]
        count[index % 10] = count[index % 10] - 1
        i = i - 1
    # print("result : " + str(result))
    '''
    Copy the result array to arr 
    '''
    k = 0    
    for i in range(len(result)):
        if result[i] > 0:
            arr[k] = result[i]
            k = k + 1 
            
    # print("arr : " + str(arr))

def radix_sort(arr):
    
    ''' Find the maximum number to know number of digits '''
    max_element = max(arr)
    exp = 1
    
    '''
     # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    '''
    while max_element // exp > 0:
        count_sort_for_radix(arr, exp)
        exp = exp * 10
    
if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66 , 33, 445,33]
    print("Array Before Sort : " + str(arr))
    radix_sort(arr)
    print("Array After radix Sort : " + str(arr))
    
