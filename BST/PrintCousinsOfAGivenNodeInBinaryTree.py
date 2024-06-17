'''
Created on 25-Oct-2016

@author: anpradha

Problem:
Print cousins of a given node in Binary Tree

Given a binary tree and a node, print all cousins of given node. Note that siblings should not be printed.

Idea is :
1. find level of given node 
2. print all nodes at a given level , The only thing to take care of is, sibling should not be printed

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLevel(root, node, level):
    if root is None:
        return 0
    
    if root == node:
        return level
    
    tempLevel = getLevel(root.left, node, level + 1)
    if tempLevel != 0:
        return tempLevel
    else:
        return getLevel(root.right, node, level + 1)


def printCousionOfGivenNode(root, node):
    level_of_node = getLevel(root, node, 1)
    
    printAlLevel(root, node, level_of_node)

def printAlLevel(root, node, level_of_node):
    
    '''if root is None or only one element is present so that level is 1 '''
    if root is None or level_of_node < 2:
        return
    
    '''If current node is parent of a node with given level'''
    if level_of_node == 2:
        ''' if node is left /right of current parent that mean its a sibling so don't consider it'''
        if root.left == node or root.right == node:
            return   
        if root.left is not None :
            print(root.left)

        if root.right is not None :
            print(root.right)
            
    #Recur for left and right subtrees     
    elif level_of_node > 2:
        printAlLevel(root.left, node, level_of_node - 1)
        printAlLevel(root.right, node, level_of_node - 1)
    
    
if __name__ == '__main__':
    pass
