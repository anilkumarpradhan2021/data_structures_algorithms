'''
Created on 22-Oct-2016

@author: anpradha

KEY : PREORDER

TOP to DOWN
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

def removeAllLeafNodes(root):
    if root is None:
        return root
    
    ''' if left and right both are none means leaf node then return Node'''
    if root.left is None and root.right is None:
        return None
    
    ''' repeat the process for left and right sub tree'''
    root.left = removeAllLeafNodes(root.left)
    root.right = removeAllLeafNodes(root.right)

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
    root = removeAllLeafNodes(root)
    inOrder(root)
    
