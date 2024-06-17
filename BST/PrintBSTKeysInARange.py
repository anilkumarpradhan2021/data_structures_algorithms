'''
Created on 22-Oct-2016

Problem:

Print BST keys in the given range

@author: anpradha

Algorithm:
1) If value of root’s key is greater than k1, then recursively call in left subtree.
2) If value of root’s key is in range, then print the root’s key.
3) If value of root’s key is smaller than k2, then recursively call in right subtree.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):    
    if root is None:
        return 0
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)

def printInRange(root, k1, k2):
    if root is None:
        return 0
    
    ''' if root.data is > k1 (lower bound) then we can expect some element from left side '''
    if root.data > k1:
        printInRange(root.left, k1, k2)
    
    '''if root.data is range between k1 and k2 print it '''
    if root.data >= k1 and root.data <= k2:
        print(root.data, end=' ')
    
    '''if root.data is < k2 (Upper bound) then we can expect some element from right side '''
    if root.data < k2:    
        printInRange(root.right, k1, k2)

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.right = Node(12)
    root.left.left = Node(4)
    inOrder(root)
    print("Print in range ")
    printInRange(root, 10, 22)
