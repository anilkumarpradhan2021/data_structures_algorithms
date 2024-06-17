'''
Created on 18-Nov-2016

@author: anpradha


Binary Indexed Tree or Fenwick Tree

Let us consider the following problem to understand Binary Indexed Tree.

We have an array arr[0 . . . n-1]. We should be able to
1 Find the sum of first i elements.
2 Change value of a specified element of the array arr[i] = x where 0 <= i <= n-1.

A simple solution is to run a loop from 0 to i-1 and calculate sum of elements. To update a value, simply do arr[i] = x.
 The first operation takes O(n) time and second operation takes O(1) time. Another simple solution is to create another 
 array and store sum from start to i at the i’th index in this array. Sum of a given range can now be calculated 
 in O(1) time, but update operation takes O(n) time now. This works well if the number of query operations are 
 large and very few updates.

Can we perform both the operations in O(log n) time once given the array?
One Efficient Solution is to use Segment Tree that does both operations in O(Logn) time.

Using Binary Indexed Tree, we can do both tasks in O(Logn) time. The advantages of Binary Indexed Tree 
over Segment are, requires less space and very easy to implement..


Check the dowloaded link for more detail
'''

def create_fenwick(arr):
    
    '''initialized all value to 0 and length is same as that of arr '''
    fenwick_Tree = [0 for _ in range(len(arr))]
    print("length of original array : " , len(arr))
    print("length of fenwick tree : " + str(len(fenwick_Tree)))
    
    ''' store actual value now using update method , we start from 1 as 1st element is added only for easy implementation'''
    for index in range(1, len(arr)):
        update(fenwick_Tree, index, arr[index])
        
    return fenwick_Tree   
    

def update(fenwick_tree, index, val):
    
    while index <= len(fenwick_tree):
        fenwick_tree[index] = fenwick_tree[index] + val
        '''update index now '''
        
        '''x & (-x) gives the last set bit in a number x '''
        index = index + (index & -index)

def get_sum(fenwick_tree, index):
    sum = 0

    while index > 0:
        sum = sum + fenwick_tree[index]
        '''update index now '''
        
        '''x & (-x) gives the last set bit in a number x '''
        index = index - (index & -index)
    
    print(sum)
    return sum
             
if __name__ == '__main__':
    '''for ease, we make sure our given array is 1-based indexed so arr[0] is 0 now '''
    print("Print original Array ")
    arr = [0, 2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    print(arr)
    
    fenwick_tree = create_fenwick(arr)
    print("Print Fenwick Tree ")
    print(fenwick_tree)
    print("Sum of element from 0 to 5")
    get_sum(fenwick_tree, 5)
    
    # update index 3 to 6
    print("update index 3 to 6")
    print("Updated Array ")
    arr[3] = arr[3] + 6
    print(arr)
    update(fenwick_tree, 3, 6)
    print("Updated Fenwick Tree ")
    print(fenwick_tree)
    print("Sum of element from 0 to 5")
    get_sum(fenwick_tree, 5)
    
    
    
