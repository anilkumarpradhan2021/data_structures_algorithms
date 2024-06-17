'''
Created on 14-Nov-2016

@author: anpradha

Segment Tree (Range Minimum Query)

Problelm :
Find the minimum number in a range 
e.g 
arr =    [1 , -2, 3 , 44, 5 , 6]
index =  [0,  1 ,  2, 3 , 4 , 5]

find minimum from index 0 to 3 , ans = -2
find minimum from index 0 to 1 , ans = -2
find minimum from index 2 to 5 , ans = 3

Time Complexity for tree construction is O(n)
Time complexity to query is O(Logn). 

Step
1. We start with a segment arr[0 . . . n-1]. and every time we divide the current segment into two halves
2. (if it has not yet become a segment of length 1)
3. then call the same procedure on both halves, 
4 . and for each such segment, we store the minimum value in a segment tree node.
5. . Leaf Nodes are the elements of the input array.


https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/

Time complexity to query is O(Logn). To query a range minimum, we process at most two nodes at every level and number of levels is O(Logn).
Time Complexity for tree construction is O(n).
The extra space required is O(n) to store the segment tree.

'''

import math
import sys


def create_segment_tree(arr, start_index, end_index, position, segment_tree):
    
    if start_index == end_index:
        segment_tree[position] = arr[start_index]
        return 
    
    mid = (start_index + end_index) // 2
    
    ''' for left child  as we know if for index i left child is 2i+1 and right child is 2*i + 2'''
    create_segment_tree(arr, start_index, mid, 2 * position + 1, segment_tree)
    
    ''' for right child '''
    create_segment_tree(arr, mid + 1, end_index, 2 * position + 2, segment_tree)
    
    '''update the parent/root min (left child, right child)'''
    segment_tree[position] = min(segment_tree[2 * position + 1], segment_tree[2 * position + 2])
    return 


def define_the_size_for_segment_tree(arr, n):    
    '''define the heigh of segment tree  log2(n) '''
    height = math.ceil(math.log(n, 2))
    print("height " , height)
    ''' total numeber of node in a complete binary tree : (2 ^ (height +1) )- 1 i.e math.pow(2,height+1) -1 '''
    max_size = 2 * pow(2, height) - 1
    return max_size


def find_the_range_minimum_util(segment_tree, start_index, end_index, search_index_start, search_index_end, position):
    
    '''check for 3 condition
    1. condition-1 if the given range is completely overlap then return the value   i.e any node start and end Index within the query search range  
    2. Partial overlap then move in both left and right child and find the min 
    3. no overlap - return a MAX value (outside the range)
     
    '''
    
    '''case - 1''' 
    if search_index_start <= start_index and end_index <= search_index_end :
        return segment_tree[position]
    
    ''' case - 3'''
    if end_index < search_index_start or search_index_end < start_index:
        return sys.maxsize
    
    '''case - 2 '''
    mid = (start_index + end_index) // 2 
    return min(find_the_range_minimum_util(segment_tree, start_index, mid, search_index_start, search_index_end, 2 * position + 1), find_the_range_minimum_util(segment_tree, mid + 1, end_index, search_index_start, search_index_end, 2 * position + 2))
    


def find_the_range_minimum(segment_tree, start_index, end_index, search_index_start, search_index_end):
    
    '''Check for erroneous input values'''
    
    if search_index_start < 0 or search_index_end > end_index or search_index_start > search_index_end:
        print("invalid input")
        return -1
    
    return find_the_range_minimum_util(segment_tree, start_index, end_index, search_index_start, search_index_end, 0)


def update_value(segment_tree, start_index, end_index, update_index, diff, position):
    
    if start_index == end_index :
        segment_tree[position] = segment_tree[position] + diff
        
    else:
        mid = (start_index + end_index) // 2
        
        '''if the update index is between start index and mid then element to update will be in left side else in right side'''
        if start_index <= update_index and update_index <= mid:
            update_value(segment_tree, start_index, mid, update_index, diff, 2 * position + 1)
        else:
            ''' need to update in right child'''
            update_value(segment_tree, mid + 1, end_index, update_index, diff, 2 * position + 2)
    
        ''' need to update the current position  from left and right child'''
        segment_tree[position] = min(segment_tree[2 * position + 1] , segment_tree[2 * position + 2])            

                
if __name__ == '__main__':
    arr = [1, 3, 2, 7, 9, 11]
    length_of_array = len(arr)
    segment_tree = []
    segment_tree_size = define_the_size_for_segment_tree(arr, length_of_array)
    print("segment_tree_size " , segment_tree_size)
    segment_tree = [None for _ in range(segment_tree_size)]
    print("print original array")
    print(arr)
    print("Segment Tree Before Create")
    print(segment_tree)
    create_segment_tree(arr, 0, length_of_array - 1, 0, segment_tree)
    print("segment Tree after ")
    print(segment_tree)
    print("find the range minimum between 1 to 5 : ")
    print(find_the_range_minimum(segment_tree, 0, length_of_array - 1, 1, 5))
    
    ''' update a value , let i want to update index 2 value form 3 to -1 '''
    update_index = 2
    new_value = -1
    diff = new_value - arr[update_index]
    
    # array is updated 
    arr[update_index] = new_value
    
    # need to update segment tree
    update_value(segment_tree, 0, length_of_array - 1 , update_index, diff, 0)
    print("print original array after update ")
    print(arr)
    print("segment Tree after update")
    print(segment_tree)
    print("find the range minimum after update between 1 to 5 : ")
    print(find_the_range_minimum(segment_tree, 0, length_of_array - 1, 1, 5))
    