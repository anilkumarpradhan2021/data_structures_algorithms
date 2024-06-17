'''
Created on 04-Jul-2017

@author: anpradha
'''


class BST():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insertNode(self, root, data):
        if root == None:
            root = BST(data)
        elif root.data >= data :
           root.left = self.insertNode(root.left, data)
        else:
            root.right = self.insertNode(root.right, data)
        return root 
            
    def inOrder(self, root):
        if root != None :
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)
                    

    def preOrder(self, root):
        if root != None :
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root != None :
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)
            
if __name__ == '__main__':
    root = BST(7)
    root.insertNode(root, 13)
    root.insertNode(root, 2)
    root.insertNode(root, 1)
    root.inOrder(root)
