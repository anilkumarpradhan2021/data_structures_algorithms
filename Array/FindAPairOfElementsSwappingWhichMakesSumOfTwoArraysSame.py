'''
Created on 19-Nov-2019

@author: anpradha

Find a pair of elements swapping which makes sum of two arrays same
Given two arrays of integers, find a pair of values (one value from each array) that you can swap to give the two arrays the same sum.

Examples:

Input: A[] = {4, 1, 2, 1, 1, 2}, B[] = (3, 6, 3, 3)
Output: {1, 3}
Sum of elements in A[] = 11
Sum of elements in B[] = 15
To get same sum from both arrays, we
can swap following values:
1 from A[] and 3 from B[]

We are looking for two values, a and b, such that: 
sumA - a + b = sumB - b + a
    2a - 2b  = sumA - sumB
      a - b  = (sumA - sumB) / 2


If arrays are sorted : O(n + m)
If arrays aren’t sorted : O(nlog(n) + mlog(m))




'''


def pair(arr1, arr2):
    sumArr1 = sum(arr1)
    sumArr2 = sum(arr2)
    
    # a - b  = (sumA - sumB) / 2
    diff = (sumArr1 - sumArr2) // 2
    
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    print("arr1 : " , arr1)
    print("arr2 : " , arr2)
    
    i = 0 
    j = 0 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] - arr2[j] == diff:
            print("Pair : " , arr1[i] , " " , arr2[j])
            return (arr1[i] , arr2[j]) 
        elif arr1[i] - arr2[j] > diff:
            j = j + 1
        else:
            i = i + 1    
    
    print("No such pair exists")    


if __name__ == '__main__':
    B = [4, 1, 2, 1, 1, 2] 
    A = [3, 6, 3, 3]
    pair(A, B) 
