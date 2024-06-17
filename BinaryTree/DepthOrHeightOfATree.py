'''
Created on 18-Oct-2016

@author: anpradha

Problem:

Write a Program to Find the Maximum Depth or Height of a Tree

 
maxDepth()
1. If tree is empty then return 0
2. Else
     (a) Get the max depth of left subtree recursively  i.e., 
          call maxDepth( tree->left-subtree)
     (a) Get the max depth of right subtree recursively  i.e., 
          call maxDepth( tree->right-subtree)
     (c) Get the max of max depths of left and right 
          subtrees and add 1 to it for the current node.
         max_depth = max(max dept of left subtree,  
                             max depth of right subtree) 
                             + 1
     (d) Return max_depth
     
     
Time Complexity: O(n)      
'''

from queue import Queue

class MyBinary(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insertData(self, root, data):
        newNode = MyBinary(data)
        if root is None:
            root = newNode
            return root
            
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node.left is not None:
                q.put(node.left)
            else:
                node.left = newNode
                return root
                
            if node.right is not None:
                q.put(node.right)
            else:
                node.right = newNode
                return root    

    def inOrder(self, root):
        if root is None:
            return 0
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1   

    ''' Approach we follow here is same as that of level Print using a Queue'''
    def maxDepthWithoutRecurssion(self, root):
        if root == None:
            return 0
        node = [root, 0]
        q = []
        q.append(node)
        max_depth = 0
        while len(q) != 0 :
            node , depth = q.pop()
            max_depth = max(max_depth, depth)
            print(max_depth)
            if node.left() is not None:
                q.append([node.left() , max_depth + 1])

            if node.right() is not None:
                q.append([node.right() , max_depth + 1])
        return max_depth       

if __name__ == '__main__':
    b = MyBinary(1)
    root = b.insertData(b, 2)
    root = b.insertData(root, 3)
    root = b.insertData(root, 4)
    root = b.insertData(root, 5)
    root = b.insertData(root, 6)
    root = b.insertData(root, 7)
    root.inOrder(root)
    print("Depth or Height Of a Tree")
    print(root.maxDepth(root))
