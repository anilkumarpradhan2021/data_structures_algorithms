'''
Created on 09-Sep-2016

@author: anpradha
'''


'''
it works when elements are in range from 1 to k.

Count sort works when the input sequence set is between a fixed range . like below


For simplicity, consider the data in the range 0 to 9. 
Input data: 1, 4, 1, 2, 7, 5, 2
  1) Take a count array to store the count of each unique object.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  2  0   1  1  0  1  0  0

  2) Modify the count array such that each element at each index 
  stores the sum of previous counts. 
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  4  4  5  6  6  7  7  7

The modified count array indicates the position of each object in 
the output sequence.
 
  3) Output each object from the input sequence followed by 
  decreasing its count by 1.
  
  Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2.
  Put data 1 at index 2 in output. Decrease count by 1 to place 
  next data 1 at an index 1 smaller than this index.


Complexity : O(n)
'''

def count_sort(arr):
    
    '''
    Create 
    result array - it will store the result of sorted list
    count array - it will store the count for elements in the set
    '''
    
    # Assuming number set is 0-10
    count = [0 for x in range(10)]
    result = [0 for x in range(10)]
    
    '''
    Update count array based on element from input arr i.e Store count of each element
    '''
    
    for i in range(len(arr)):
        count[arr[i]] = count[arr[i]] + 1 
    
    
    '''
     Change count[i] so that count[i] now contains actual position of this character in output array
    
    '''
    for i in range(1, len(count)):
        count[i] = count[i - 1] + count[i]
    
    '''
    update result array 
    '''
    #print(count)
    i = len(arr) - 1
    while i >= 0:
        result[count[arr[i]]] = arr[i]
        count[arr[i]] = count[arr[i]] - 1
        i = i - 1
        #print("result" , result)
        #print("count" , count)


    
    '''
    Copy the result array to arr 
    '''
    k = 0    
    for i in range(len(result)):
        if result[i] > 0:
            arr[k] = result[i]
            k = k + 1 
        
    print("count " , count)
    print("result" , result)
    

if __name__ == '__main__':
    arr = [1, 4, 1, 2, 7, 5, 2]
    print("Array Before Sort : " + str(arr))
    count_sort(arr)
    print("Array After count Sort : " + str(arr))
