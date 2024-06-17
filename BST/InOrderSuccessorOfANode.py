'''
Created on 19-Oct-2016

@author: anpradha

Problem :

Inorder Successor in Binary Search Tree


1) If right subtree of node is not NULL, then succ lies in right subtree. Do following.
Go to right subtree and return the node with minimum key value in right subtree.

2) If right sbtree of node is NULL, then succ is one of the ancestors. Do following.
Travel up using the parent pointer until you see a node which is left child of it’s parent. The parent of such a node is the succ.



'''

class BST(object):
    '''
    classdocs
    '''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
     
    ''' insert a node into BST '''    
    def insert_bst(self, root, data):
        if root == None:
            root = BST(data)
            return root
        
        if data > root.data:
            if root.right is None:
                root.right = BST(data)
                return
            root.right.insert_bst(root.right, data)
        else:
            if root.left is None:
                root.left = BST(data)
                return
            root.left.insert_bst(root.left, data)   
            
    ''' inorder traversal of a tree '''              
    def inOrder(self, root):
        if root is None :
            return
        self.inOrder(root.left)
        print(root.data, end=' ')
        self.inOrder(root.right)    
        
    ''' find a node in binary tree '''
    def findNode(self, root, val):
        if root.data == val:
            return root
        if val > root.data:
            return self.findNode(root.right, val)
        else:
            return self.findNode(root.left, val)
        
        return None
    
    ''' find the minimum of a node '''
    def findMin(self, node):
        while node.left:
            node = node.left
        return node    
    
    '''1) If right subtree of node is not NULL, then succ lies in right subtree. 
        Do following.
            Go to right subtree and return the node with minimum key value in right subtree.
        2) If right sbtree of node is NULL, then start from root and us search like technique. 
        Do following.
            Travel down the tree, if a node’s data is greater than root’s data then go right side, otherwise go to left side.'''
                
    def inOrderSuccessorOfNode(self, root, node):
        if node.right is not None:
            return self.findMin(node.right)
        
        succ = None
        temp = root
        while temp is not None:
            if node.data > temp.data:
                succ = temp
                temp = temp.right
            elif node.data < temp.data:
                succ = temp
                temp = temp.left
            else:
                break 
        
        return succ       
                    
                      
                 
                    

if __name__ == '__main__':
    root = BST(10)
    root.insert_bst(root, 8)
    root.insert_bst(root, 19)
    root.insert_bst(root, 29)
    root.insert_bst(root, 30)
    root.insert_bst(root, 27)
    root.insert_bst(root, 7)
    root.inOrder(root)
    t = root.findNode(root, 29)
    print(t.data)
    t = root.inOrderSuccessorOfNode(root, t)
    print(t.data)
    
