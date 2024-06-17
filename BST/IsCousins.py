'''
Created on 24-Oct-2016

@author: anpradha
Problem: 
Check if two nodes are cousins in a Binary Tree

The idea is to find level of one of the nodes. Using the found level, check if ‘a’ and ‘b’ are at this level. 
If ‘a’ and ‘b’ are at given level,  then finally check if they are not children of same parent.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSibling(root, node1, node2):
    if root is None:
        return False
    if root.left == node1 and root.right == node2 or root.left == node2 and root.right == node1 or isSibling(root.left, node1, node2) or isSibling(root.right, node1, node2):
        return True
    return False

def levelOfNode(root, node, level):
    if root is None :
        return 0
    ''' if data match break it '''
    if root == node:
        return level
    
    '''1st find in left tree  if found then level wont be zero so return else find in right side'''
    tempLevel = levelOfNode(root.left, node, level + 1) 
    if tempLevel != 0:
        return tempLevel
    
    '''else search in right subtree'''
    return levelOfNode(root.right, node, level + 1)

def isCousions(root, node1, node2):
    
    '''
    The two nodes should be on the same level in the binary tree
    # The two nodes should not be siblings(means that 
    # they should not have the same parent node'''
    if levelOfNode(root, node1, 0) == levelOfNode(root, node2, 0) and not isSibling(root, node1, node2):
        return True
    else:
        return False
    
if __name__ == '__main__':
    root = Node(6)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.left = Node(1)
    root.right.right = Node(3)
    
    node1 = root.left.right # 8
    node2 = root.right.right # 3
    
    print(isCousions(root, node1, node2))
    
    
    node1 = root.left.right # 8
    node2 = root.left.left # 7
 
    print(isCousions(root, node1, node2))
    
    
    
