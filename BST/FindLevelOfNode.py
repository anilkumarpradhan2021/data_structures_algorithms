'''
Created on 24-Oct-2016

@author: anpradha

Problem: 
Get Level of a node in a Binary Tree

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOfNodeBST(root, data, level):
    if root is None :
        return 0
    if root.data == data:
        return level
    if data > root.data:
        return levelOfNodeBST(root.right, data, level + 1) 
    else:
        return levelOfNodeBST(root.left, data, level + 1)

def levelOfNode(root, data, level):
    if root is None :
        return 0
    ''' if data match break it '''
    if root.data == data:
        return level
    
    '''1st find in left tree  if found then level wont be zero so return else find in right side'''
    tempLevel = levelOfNode(root.left, data, level + 1) 
    if tempLevel !=0:
        return tempLevel
    tempLevel = levelOfNode(root.right, data, level + 1)
    return tempLevel


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(15)
    root.left.left = Node(4)
    root.left.right = Node(9)
    root.right.right = Node(18)
    print(levelOfNodeBST(root, 18, 0))
    print(levelOfNode(root, 18, 0))

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.left.left = Node(6)
    print(levelOfNode(root, 5, 0))
