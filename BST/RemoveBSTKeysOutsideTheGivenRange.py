'''
Created on 22-Oct-2016

@author: anpradha

Problem:

Remove BST keys outside the given range
There are two possible cases for every node.
1) Node’s key is outside the given range. This case has two sub-cases.
…….a) Node’s key is smaller than the min value.
…….b) Node’s key is greater that the max value.
2) Node’s key is in range.

We don’t need to do anything for case 2. In case 1, we need to remove the node and change root of sub-tree rooted with this node.
The idea is to fix the tree in Postorder fashion. When we visit a node, we make sure that its left and right sub-trees are
 already fixed. 
 In case 1.a), we simply remove root and return right sub-tree as new root. 
 In case 1.b), we remove root and return left sub-tree as new root.


Time Complexity: O(n) where n is the number of nodes in given BST.

KEY :  POSTORDER

BOTTOM to TOP approach 

'''

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
    print(root.data,end=" ")
    inOrder(root.right)


'''Removes all nodes having value outside the given range and returns the root of modified tree'''
def removeBSTOutsideGivenrRange(root,k1,k2):
    if root is None:
        return root
    
    '''First fix the left and right subtrees of root'''
    root.left = removeBSTOutsideGivenrRange(root.left, k1, k2)
    root.right = removeBSTOutsideGivenrRange(root.right, k1, k2)
    
    '''Now fix the root.  There are 2 possible cases for root
       1.a) Root's key is smaller than min value (root is not in range)'''
    if root.data < k1:
        right  = root.right
        return right
    
    '''1.b) Root's key is greater than max value (root is not in range)'''
    if root.data > k2:
        left  = root.left
        return left
    
    '''2. Root is in range'''
    return root    
                                
if __name__ == '__main__':
    root = None
    root = insert_node(root, 6)
    insert_node(root, -13)
    insert_node(root, 14)
    insert_node(root, -8)
    insert_node(root, 13)
    insert_node(root, 15)
    insert_node(root, 7)
    inOrder(root)
    print("\nPrint After remove :")
    removeBSTOutsideGivenrRange(root, -10, 13)
    inOrder(root)
    
    
    
    
    
