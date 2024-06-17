'''
Created on 24-Sep-2019

@author: anpradha

Smallest Difference pair of values between two unsorted Arrays
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.

Examples :

Input : A[] = {l, 3, 15, 11, 2}
        B[] = {23, 127, 235, 19, 8} 
Output : 3  
That is, the pair (11, 8) 

Input : A[] = {l0, 5, 40}
        B[] = {50, 90, 80} 
Output : 10
That is, the pair (40, 50)

Consider the following two arrays:
A: {l, 2, 11, 15}
B: {4, 12, 19, 23, 127, 235}

1. Suppose a pointer a points to the beginning of A and a pointer b points to the beginning of B. The current difference between a and bis 3. Store this as the min.

2. How can we (potentially) make this difference smaller? Well, the value at b is bigger than the value at a, so moving b will only make the difference larger. Therefore, we want to move a.

3. Now a points to 2 and b (still) points to 4. This difference is 2, so we should update min. Move a, since it is smaller.

4. Now a points to 11 and b points to 4. Move b.

5. Now a points to 11 and b points to 12. Update min to 1. Move b. And so on.


'''


def smallestDifferencePairOfValuesBetweenTwoUnsortedArrays(arr1, arr2):
    # need to sort both the arrray 
    
    arr1.sort()
    arr2.sort()
    smallest_diff = float("inf")
    a = 0  # position tracker for arr1
    b = 0  # position tracker for arr2
    
    while a < len(arr1) and b < len(arr2):
        smallest_diff = min(smallest_diff, abs(arr1[a] - arr2[b]))
                
        if arr1[a] < arr2[b]:
            a = a + 1
        else:
            b = b + 1     


        
    print("smallest_diff : " , smallest_diff)    

    
if __name__ == '__main__':
    arr1 = [1, 3, 15, 11, 2]
    arr2 = [23, 127, 235, 19, 8]
    smallestDifferencePairOfValuesBetweenTwoUnsortedArrays(arr1, arr2)
