'''
Created on 25-Oct-2016

@author: anpradha

Problem:

Print all nodes that don’t have sibling

Given a Binary Tree, print all nodes that don’t have a sibling (a sibling is a node that has same parent. 
In a Binary Tree, there can be at most one sibling). Root should not be printed as root cannot have a sibling.

Time Complexity of above code is O(n) as the code does a simple tree traversal.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printAllNodeHaveNoSibling(root):
    
    '''Base Case'''
    if root is None :
        return
    
    '''If this is an internal node , recur for left and right subtree'''
    if root.left is not None and root.right is not None :
        printAllNodeHaveNoSibling(root.left)
        printAllNodeHaveNoSibling(root.right)
    
    #    '''If left child is NULL, and right is not, print right child and recur for right child'''
    elif root.right is not None:
        print(root.right.data,end=' ')
        printAllNodeHaveNoSibling(root.right)     

    #''' If right child is NULL and left is not, print left child and recur for left child'''
    elif root.left is not None:
        print(root.left.data,end=' ')
        printAllNodeHaveNoSibling(root.left)     
        
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.left.left = Node(6)
    printAllNodeHaveNoSibling(root)
