'''
Created on 14-Nov-2016

@author: anpradha

Segment Tree (Sum of given range same logic as Range Minimum Query)

Problem :
Find the sum a given range in an array in O(long) time 
e.g 
arr =    [1, 3, 5, 7, 9, 11]
index =  [0, 1, 2, 3, 4 , 5]

find sum from index 0 to 3 , ans = 16
find sum from index 1 to 3 , ans = 15

Time Complexity for tree construction is O(n)
Time complexity to query is O(Logn). 


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
    
    '''update the parent/root left child + right child '''
    segment_tree[position] = segment_tree[2 * position + 1] + segment_tree[2 * position + 2]
    return 

def define_the_size_for_segment_tree(arr, n):    
    '''define the size of segment tree '''
    size = math.ceil(math.log(n) / math.log(2))
    max_size = 2 * pow(2, size) - 1
    return max_size

def sum_of_given_range_util(segment_tree, start_index, end_index, search_index_start, search_index_end, position):
    
    '''check for 3 condition
   
    To query on a given range, check 3 conditions.

        Case -1 Range represented by a node is completely inside the given range
        Case-2 Range represented by a node is partially inside and partially outside the given range
        Case-3 Range represented by a node is completely outside the given range
        
    '''
    
    '''case - 1 range represented by a node is completely inside the given range ''' 
    if search_index_start <= start_index and end_index <= search_index_end :
        return segment_tree[position]
    
    
    ''' case - 3  range represented by a node is completely outside the given range '''
    if end_index < search_index_start or search_index_end < start_index:
        return 0
    
    '''case - 2  range represented by a node is partially inside and partially outside the given range'''
    mid = (start_index + end_index) // 2 
    return (sum_of_given_range_util(segment_tree, start_index, mid, search_index_start, search_index_end, 2 * position + 1) + sum_of_given_range_util(segment_tree, mid + 1, end_index, search_index_start, search_index_end, 2 * position + 2))
    

def sum_of_given_range(segment_tree, start_index, end_index, search_index_start, search_index_end):
    
    '''Check for erroneous input values'''
    
    if search_index_start < 0 or search_index_end > end_index or search_index_start > search_index_end:
        print("invalid input")
        return -1
    
    return sum_of_given_range_util(segment_tree, start_index, end_index, search_index_start, search_index_end, 0)


                
if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11]
    length_of_array = len(arr)
    segment_tree = []
    segment_tree_size = define_the_size_for_segment_tree(arr, length_of_array)
    segment_tree = [None for _ in range(segment_tree_size)]
    print("print original array")
    print(arr)
    print("Segment Tree Before Create")
    print(segment_tree)
    create_segment_tree(arr, 0, length_of_array - 1, 0, segment_tree)
    print("segment Tree after ")
    print(segment_tree)
    print("find the range minimum between 1 to 3 : ")
    print(sum_of_given_range(segment_tree, 0, length_of_array - 1, 1, 3))
    
    
    
     
    
    
