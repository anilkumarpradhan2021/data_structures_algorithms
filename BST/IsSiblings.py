'''
Created on 24-Oct-2016

@author: anpradha
Problem:
In a Binary Tree, Check if Two nodes has the same parent or are siblings

Objec­tive: In a Binary Tree, Check if Two nodes has the same par­ent or are siblings


Approach:

    Given, root, Node x, Node y.
    Check if x and y are child of root.   
    if root.left==x && root.right==y or root.left==y && root.right==x
        then return true.
    Else 
        make a recur­sive call to root.left and root.right


'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSibling(root, node1, node2):
    if root is None:
        return False
    if root.left and root.right:
        if root.left == node1 and root.right == node2 or root.left == node2 and root.right == node1 or isSibling(root.left, node1, node2) or isSibling(root.right, node1, node2):
            return True
    return False
    
if __name__ == '__main__':
    root = Node(10)
    node1 = root.left = Node(8)
    node2 = root.right = Node(15)
    print("node1 and node2 Sibling ? ")
    print(isSibling(root, node1, node2))

    node3 = root.left.left = Node(4)
    node4 = root.left.right = Node(9)
    
    print("node3 and node4 Sibling ? ")
    print(isSibling(root, node3, node4))

    print("node3 and node2 Sibling ?")
    print(isSibling(root, node3, node2))
