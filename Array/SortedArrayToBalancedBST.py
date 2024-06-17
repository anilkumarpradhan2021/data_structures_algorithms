'''
Created on 01-Oct-2019

@author: anpradha
Sorted Array to Balanced BST
Given a sorted array. Write a function that creates a Balanced Binary Search Tree using array elements.
Examples:

Input:  Array {1, 2, 3}
Output: A Balanced BST
     2
   /  \
  1    3 

Input: Array {1, 2, 3, 4}
Output: A Balanced BST
      3
    /  \
   2    4
 /
1

ALGO:

1) Get the Middle of the array and make it root.
2) Recursively do same for left half and right half.
      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1.
          

Time Complexity: O(n)
          
          
'''


from queue import Queue
from typing import List


class Node():

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

'''
    Recurssive way
'''        
def sortedArrayToBST(arr):
    if len(arr) == 0:
        return None
    
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid + 1:])
    
    return root

'''
    Iterative way
'''
def iterative_sorted_array_to_bst(arr: List[int]) -> Node:
    if len(arr) == 0:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    q=Queue()
    q.put((root,0,mid-1))
    q.put((root,mid+1,len(arr)-1))
    
    while not q.empty():
        current = q.get()
        print(current)
        current_node = current[0]
        left_index = current[1]
        right_index = current[2]
        
        if left_index <= right_index and current_node is not None:
            mid = (left_index + right_index ) //2
            child_node = Node(arr[mid])
            
            if child_node.data <= current_node.data:
                current_node.left = child_node
            else:
                current_node.right = child_node
            q.put((child_node,left_index,mid-1))
            q.put((child_node,mid+1,right_index))
    return root
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7] 
    #arr = [1, 2, 3, 4, 5, 6] 
    #arr = [1, 2, 3] 
    #arr = [1, 2, 3, 4] 
    #root = sortedArrayToBST(arr)
    root = iterative_sorted_array_to_bst(arr)
    preOrder(root)
