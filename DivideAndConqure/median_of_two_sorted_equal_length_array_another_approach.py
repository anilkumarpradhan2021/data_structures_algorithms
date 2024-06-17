'''
Created on 21-Sep-2016

@author: anpradha

Problem :
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).


This problem can be converted to the problem of finding kth element, 
k is (A's length + B' Length)/2.

Cases to handle :
CASE 1: 
If any of the two arrays is empty, then the kth element is the non-empty array's kth element.
CASE 2 :
If k == 0, the kth element is the first element of A or B.
CASE 3:
For normal cases(all other cases), we need to move the pointer at the pace of half of the array size to get log(n) time


if not able to understand JUST MUG it :) 
i + j = k - 1 or i + j + 1 = k
 
As for why aMid + bMid + 1 = k is significant: If A[aMid] is less than B[bMid], you know that any elements in after A[aMid] in A can't
 be the kth element since there are too many elements in B lower than it (and would exceed k elements). 
 You also know that B[bMid] and any element before B[bMid] in B can't be the kth element since there are too 
 few elements in A lower than it (there wouldn't be enough elements before B[bMid] to be the kth element).
 
 
 
(1) aMid = aLen / 2, 
(2)  k = (aLen + bLen) / 2  
2k = (aLen + bLen) which means
(3) 2 = (aLen + bLen) / k
then, just substitute (3) to (1)

'''

def median_of_sorted_arrays(A, B):
    m = len(A)
    n = len(B)
    total = m + n
    if (total) % 2 == 0:  # even
        return  (findKth(A, B, (total // 2), 0, 0, m - 1, n - 1) + findKth(A, B, ((total - 1) // 2), 0, 0, m - 1, n - 1)) // 2
    else:  # odd
        return findKth(A, B, (total // 2), 0, 0, m - 1, n - 1)


def findKth(A, B, k, aStart, bStart, aEnd, bEnd):
    
    aLength = aEnd - aStart + 1
    bLength = bEnd - bStart + 1
    
    ''' Handle special cases '''
    if aLength == 0:
        return B[bStart + k]  # if len(A) is zero then kth element will be in B only 
    
    if bLength == 0:
        return A[aStart + k]  # Same as above
    
    if k == 0:
        return  min(A[aStart], B[bStart])
    
    aMid = (k * aLength) // (aLength + bLength)  # See above explanation how to derive it
    bMid = k - aMid - 1  # aMid+ bMid = k - 1
    
    ''' make aMid and bMid to be array index'''
    
    aMid = aMid + aStart
    bMid = bMid + bStart
    

    if A[aMid] > B[bMid]:
        k = k - (bMid - bStart + 1)  
        aEnd = aMid
        bStart = bMid + 1
    else:
        k = k - (aMid - aStart + 1)
        aStart = aMid + 1
        bEnd = bMid  
        
    return findKth(A, B, k, aStart, bStart, aEnd, bEnd)   
     
        

if __name__ == '__main__':
    arr1 = [1, 12, 15, 26, 38]
    arr2 = [2, 13, 17, 30, 45]
    print(median_of_sorted_arrays(arr1, arr2))
