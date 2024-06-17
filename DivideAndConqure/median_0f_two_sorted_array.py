'''
Created on 21-Sep-2016

@author: anpradha
Time Complexity : O(n)


'''

def median_of_two_sorted_equal_length_array(arr1, arr2):
    i = 0  # Current index of i/p array ar1[]
    j = 0;  # Current index of i/p array ar2[]
    m1 = -1
    m2 = -1
    '''  as n + n  = 2n means whether its even + even  or odd + odd , total array will be even , so for even (n+(n+1))/2, so one more than half 
    Since there are 2n elements, median will be average of elements at n and n + 1 in the array obtained after
     merging ar1 and ar2
    '''
    for _ in range(len(arr1) + 1):

        ''' Below is to handle case where all elements of ar1[] are
          smaller than smallest(or first) element of ar2[] '''
        if i == len(arr1):
            m1 = m2
            m2 = arr2[0]
            break
        # Below is to handle case where all elements of ar2[] are smaller than smallest(or first) element of ar1[]
        elif j == len(arr2):
            m1 = m2
            m2 = arr1[0]
            break
            
        if arr1[i] < arr2[j]:
            m1 = m2  # Store the prev median
            m2 = arr1[i]
            i = i + 1
        else:
            m1 = m2  # Store the prev median
            m2 = arr2[j]
            j = j + 1
        print(m1)
        print(m2)    
    return (m1 + m2) / 2

                
if __name__ == '__main__':
    arr1 = [1, 12, 15, 26, 38]
    arr2 = [2, 13, 17, 30, 45]
    print(median_of_two_sorted_equal_length_array(arr1, arr2))
