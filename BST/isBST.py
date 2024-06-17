'''
Created on 20-Oct-2016

@author: anpradha


Problem:
A program to check if a binary tree is BST or not

Time Complexity: O(n)
'''


INT_MAX = 4294
INT_MIN = -4294
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
        

'''' Return true if the given tree is a BST and its values # >= min and <= max '''    
def isBSTUtil(node, minimum, maximum):
     
    '''An empty tree is BST'''
    if node is None:
        return True
 
    '''False if this node violates min/max constraint'''
    if node.data < minimum or node.data > maximum:
        return False

    ''' Otherwise check the subtrees recursively , tightening the min or max constraint ''' 
    return (isBSTUtil(node.left, minimum, node.data -1) and isBSTUtil(node.right, node.data+1, maximum))
     

''' Returns true if the given tree is a binary search tree (efficient version) '''
def isBST(node):
    return (isBSTUtil(node, float("-inf"), float("inf")))
     
        
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
     
    if (isBST(root)):
        print("Is BST")
    else:
        print("Not a BST")