'''
Created on 14-Oct-2019

@author: anpradha

Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path  
# exists otherwise false 


'''


class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def findPath(self, root, data, path):
        if root is None:
            return False
        
        path.append(root.data)
        if root.data == data:
            return True
        if root.left and self.findPath(root.left, data, path) or root.right and self.findPath(root.right, data, path):
            return True
 
        # If not present in subtree rooted with root, remove 
        # root from path and return False 
       
        path.pop()
        return False
        


if __name__ == '__main__':
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    path = []
    print(root.findPath(root, 7, path))
    print("path : " , path)

    path = []    
    print(root.findPath(root, 9, path))
    print("path : " , path)