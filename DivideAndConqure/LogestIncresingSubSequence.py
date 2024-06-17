'''
Created on 26-Sep-2016

@author: anpradha

Problem :
Longest Increasing Subsequence Size (N log N)

Our strategy determined by the following conditions,

1. If A[i] is smallest among all end 
   candidates of active lists, we will start 
   new active list of length 1.
   
2. If A[i] is largest among all end candidates of 
  active lists, we will clone the largest active 
  list, and extend it by A[i]. i.e add A[i] to largest active list

3. If A[i] is in between, we will find a list with 
  largest end element that is smaller than A[i]. 
  Clone and extend this list by A[i]. We will discard all
  other lists of same length as that of this modified list.


THIS WILL JUST GIVE YOU THE COUNT , NOT THE ACTUAL ARRAY 

complexity : O(nlogn)



'''
def CeilIndex(A, r, key):
    
    ''' Using binary search '''
    low = 0
    high = r
    while low <= high:
        mid = (low + high) // 2
        if A[mid] >= key:
            return mid
        else:
            low = mid + 1
    return -1    

def LongestIncreasingSubsequenceLength(A, size):

    tailTable = [-float('inf') for _ in range(size)];
    tailTable[0] = A[0];
    len = 1;
    for i in range(1, size):
        ''' if start index of list is less than A[i] , then update the start index'''
        if A[i] < tailTable[0]:
            # new smallest value
            tailTable[0] = A[i];
        
        # IF A[i] is greater than previous element then add it    
        elif A[i] > tailTable[len - 1]:
            # A[i] wants to extend largest subsequence
            tailTable[len] = A[i];
            len = len + 1
        # if A[i] is in between     
        else:
            # A[i] wants to be current end candidate of an existing
            # subsequence. It will replace ceil value in tailTable
            tailTable[CeilIndex(tailTable, len - 1, A[i])] = A[i];
            
        print(tailTable)  
    return len;
 

if __name__ == '__main__':
    A = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print("A : " + str(A))
    n = len(A)
    print(LongestIncreasingSubsequenceLength(A, n))
    

    A = [10,18, 11, 4]
    print("A : " + str(A))
    n = len(A)
    print(LongestIncreasingSubsequenceLength(A, n))
