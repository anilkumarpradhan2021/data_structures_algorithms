'''
Created on 22-Oct-2016

@author: anpradha
Problem :
1.  find if BST is a AVL Tree or not
2. How to determine if a binary tree is height-balanced?



An empty tree is height-balanced. A non-empty binary tree T is balanced if:
1) Left subtree of T is balanced
2) Right subtree of T is balanced
3) The difference between heights of left subtree and right subtree is between -1 t0 1

'''


# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def getBalance(node):
    if node is None:
        return 0
    else:
        return height(node.left) - height(node.right)
             

def height(node):
    if node is None :
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))        
    
def isAvl(root):
    if root is None:
        return True
    balance = getBalance(root)
    if balance > 1 or balance < -1:
        return False   
    else:
        return isAvl(root.left) and isAvl(root.right)     
    


if __name__ == '__main__':
    root = Node(4)
    # root.left = Node(2)
    root.right = Node(5)
    root.right.right = Node(6)
    # root.left.left = Node(1)
    # root.left.right = Node(3)
    print(isAvl(root))
