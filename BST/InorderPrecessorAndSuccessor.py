'''
Created on 19-Oct-2016

@author: anpradha

Problem :
Inorder predecessor and successor for a given key in BST


Input: root node, key
output: predecessor node, successor node

1. If root is NULL
      then return
2. if key is found then
    a. If its left subtree is not null
        Then predecessor will be the right most child of left subtree or left child itself.
    b. If its right subtree is not null
        The successor will be the left most child of right subtree or right child itself.
    return
3. If key is smaller then root node
        set the successor as root , search recursively into left subtree
    else
        set the predecessor as root , search recursively into right subtree




'''

class BST(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_bst(root, data):
    if root == None:
        root = BST(data)
        return root
    
    if data > root.data:
        root.right = insert_bst(root.right, data)
    else:
        root.left = insert_bst(root.left, data)   
    
    return root    

''' inorder traversal of a tree '''              
def inOrder(root):
    if root is None :
        return
    inOrder(root.left)
    print(root.data, end=' ')
    inOrder(root.right)    


def findSuccessorAndPrecessor(root, val, successor, precessor):
    '''Base case'''
    if root is None:
        return
     
    if root.data == val:
        
        '''the minimum value in right subtree is successor'''
        if root.right is not None:
            temp = root.right
            while temp.left:
                temp = temp.left
            successor = temp
        
        '''the maximum value in left subtree is predecessor'''    
        if root.left is not None:
            temp = root.left
            while temp.right:
                temp = temp.right
            precessor = temp
        return (successor, precessor)

    elif val > root.data:
        '''     //  we make the root as predecessor because we might have a
                // situation when value matches with the root, it wont have
                // right subtree to find the predecessor, in that case we need
                // parent to be the predecessor. 
        '''
        precessor = root
        findSuccessorAndPrecessor(root.right, val, successor, precessor)
    else:
        '''
                // we make the root as successor because we might have a
                // situation when value matches with the root, it wont have
                // right subtree to find the successor, in that case we need
                // parent to be the successor      
        '''
        successor = root    
        findSuccessorAndPrecessor(root.left, val, successor, precessor)
                    
                
                
    
    
if __name__ == '__main__':
    root = None
    root = insert_bst(root, 10)
    insert_bst(root, 8)
    insert_bst(root, 19)
    insert_bst(root, 29)
    insert_bst(root, 30)
    insert_bst(root, 27)
    insert_bst(root, 7)
    inOrder(root)
    prec = None
    succ = None
    prec, succ = findSuccessorAndPrecessor(root, 10, prec, succ)
    print(succ.data)
    print(prec.data)
    
