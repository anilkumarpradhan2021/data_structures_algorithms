'''
Created on 22-Oct-2016

@author: anpradha


Find the closest element in Binary Search Tree

Given a binary search tree and a target node K. The task is to find the node with minimum absolute difference with given target value K.


Algorithm to find closest node in binary search tree:
1. Start from root, initialize min to MAX_INT.
2. If currentNode value is equal to given value, return currentNode.
3. If difference between currentNode and given value is less than minimum,  update minimum 
3. Check if given value is less than currentNode value
   3.1 search closest node in left subtree.
4. If given value is greater than currentNode value, 
   4.1 search closest node in right subtree. 

Take care while comparing minimum value and difference and storing minimum value. We need to store minimum value with sign

Complexity :
Average complexity of this algorithm to find closest node in binary search tree is O(logN), 
but if the tree is completely skewed, i.e worst case complexity will be O(N).


'''

import sys
from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    if root == None:
        root = Node(data)
    else:
        if data > root.data:
            root.right = insert_node(root.right, data)
        else:
            root.left = insert_node(root.left, data)
    return root        


def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


''' Idea is we have a gloabal variable which have the maximum value then for each node in tree we update the the closest '''


minumum = sys.maxsize


def findClosest(root, val):
    global minumum
    
    if root is None :
        return
    
    ''' if minimum is greater then current difference , update it'''
    if abs(minumum) > abs(root.data - val):
        minumum = root.data - val
    
    if val >= root.data:
        findClosest(root.right, val)
    else:
        findClosest(root.left, val)  

    
def findClosest2(root, val, minumum, element):
    
    if root is None :
        return
    
    ''' if minimum is greater then current difference , update it'''
    if abs(minumum) > abs(root.data - val):
        minumum = root.data - val
        element[-1] = root.data
    
    if val >= root.data:
        findClosest2(root.right, val, minumum, element)
    else:
        findClosest2(root.left, val, minumum, element)  


def findClosestWithOutRecursion(root, val):
    
    if root is None:
        print("Not possible") 
    
    queue = Queue()
    queue.put(root)
    minimum_val = sys.maxsize
    element = None
    
    while not queue.empty() :
        node = queue.get()
        
        if abs(minimum_val) > abs(node.data - val):
            minimum_val = node.data - val
            element = node
        
        if node.left is not None:
            queue.put(node.left)
                
        if node.right is not None:
            queue.put(node.right)
    
    print("Closest element : " + str(element.data))


if __name__ == '__main__':
    root = None
    root = insert_node(root, 30)
    insert_node(root, 20)
    insert_node(root, 15)
    insert_node(root, 25)
    insert_node(root, 40)
    insert_node(root, 37)
    insert_node(root, 45)
    inOrder(root)
    number = 29
    print("\nNumber is : " + str(number))
    print("Closest Number is : ")
    findClosest(root, number)
    print(number + minumum)
    findClosestWithOutRecursion(root, 30)
    element = [None]
    findClosest2(root, 30, sys.maxsize, element)
    print("Last : " , element)
