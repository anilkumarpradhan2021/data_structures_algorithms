'''
Created on 18-Oct-2016

@author: anpradha
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

    def ancestorOfNode(self, root, val):
        '''base cases '''
        if root is None:
            return False
        
        if root.data == val:
            return True
        
        '''If target is present in either left or right subtree of this node, then print this node'''
        if self.ancestorOfNode(root.left, val) or self.ancestorOfNode(root.right, val):
                print(root.data, end=" ")
                return True
                
        return False        
                
if __name__ == '__main__':
    b = MyBinary(1)
    root = b.insertData(b, 2)
    root = b.insertData(root, 3)
    root = b.insertData(root, 4)
    root = b.insertData(root, 5)
    root = b.insertData(root, 6)
    root = b.insertData(root, 7)
    root.inOrder(root)
    print("Ancestor Of Node")
    root.ancestorOfNode(root, 7)
