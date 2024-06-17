'''
Created on 22-Oct-2016

@author: anpradha
Problem : 
Remove all the half nodes in Binary Tree 

The idea is to use post-order traversal to solve this problem efficiently. 
We first process the 
    1 . left children, 
    2.  then right children, 
    3. and finally the node itself. 
So we form the new tree bottom up, starting from the leaves towards the root. By the time we process the current node, 
both its left and right subtrees were already processed. Below is the implementation of this idea.


KEY :  POSTORDER

Note :
This solution is applicable for Binary Search Tree.
It will work for Binary Tree if we modify insert node function

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

def removeAllhalfNodes(root):
    if root is None:
        return root
    
    '''First fix the left and right subtrees of root'''
    root.left = removeAllhalfNodes(root.left)
    root.right = removeAllhalfNodes(root.right)
    

    ''' if both left and right child is None the node is not a Half node '''
    if root.left is None and root.right is None:
        return root
    
    '''if current nodes is a half node with left
       child NULL left, then it's right child is
       returned and replaces it in the given tree'''
    if root.left is None:
        right  = root.right
        root  = None
        del root
        return right

    '''if current nodes is a half node with right
       child NULL right, then it's right child is
       returned and replaces it in the given tree '''
    if root.right is None:
        left  = root.left
        root  = None
        del root
        return left
    
    return root    
    
if __name__ == '__main__':
    root = None
    root = insert_node(root, 2)
    insert_node(root, 7)
    insert_node(root, 5)
    insert_node(root, 6)
    insert_node(root, 1)
    insert_node(root, 11)
    insert_node(root, 9)
    insert_node(root, 4)
    inOrder(root)
    print("\nPrint after removing all half nodes")
    root = removeAllhalfNodes(root)
    inOrder(root)
    

