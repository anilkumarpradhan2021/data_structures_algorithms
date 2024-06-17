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


    def existanceOfGivenSum(self, root, val, current_path, paths):
        if root is None :
            return False
        
        current_path = current_path + [root.data]
        if root.data == val:
            paths.append(current_path)
            return True
        
        return self.existanceOfGivenSum(root.left, val - root.data , current_path, paths) or self.existanceOfGivenSum(root.right, val - root.data, current_path, paths)     

    def printExistanceOfGivenSum(self, root, val):
        current_path = []
        paths = []
        print("Path Exits or not : " + str(self.existanceOfGivenSum(root, val, current_path, paths)))
        print("Path exists : " + str(paths))

if __name__ == '__main__':
    b = MyBinary(1)
    root = b.insertData(b, 2)
    root = b.insertData(root, 3)
    root = b.insertData(root, 4)
    root = b.insertData(root, 5)
    root = b.insertData(root, 6)
    root = b.insertData(root, 7)
    root.inOrder(root)
    root.printExistanceOfGivenSum(root, 11)
