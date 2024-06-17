'''
Created on 18-Oct-2016

@author: anpradha

'''
class Node(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1
    
    ''' get the height of the node'''
    def nodeHeight(self, node):
        if node == None:
            return 0
        else:
            return node.height 
    
    '''get Balance factor of a node i.e height(node.left) - height(node.right)'''
    def getBalance(self, node):
        if node == None:
            return 0
        else:
            return (self.nodeHeight(node.left) - self.nodeHeight(node.right))    
    
    ''' rotate towards right side '''
    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        
        '''Perform rotation'''
        x.right = y
        y.left = T2
        
        '''Update heights'''
        x.height = max(self.nodeHeight(x.left), self.nodeHeight(x.right)) + 1
        y.height = max(self.nodeHeight(y.left), self.nodeHeight(y.right)) + 1
        
        '''Return new root'''
        return x
        
    ''' rotate towards left side'''
    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        
        '''Perform rotation'''
        y.left = x
        x.right = T2
        
        '''Update heights'''
        x.height = max(self.nodeHeight(x.left), self.nodeHeight(x.right)) + 1
        y.height = max(self.nodeHeight(y.left), self.nodeHeight(y.right)) + 1
        
        '''Return new root'''
        return y
    
    ''' Insert a Node into BST '''          
    def insert(self, root, data):
        
        '''1.  Perform the normal BST rotation'''
        if root is None:
            root = Node(data)
            return root
        if root.data > data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        '''2. Update height of this ancestor node'''
        root.height = max(self.nodeHeight(root.left), self.nodeHeight(root.right)) + 1
        
        '''3. Get the balance factor of this ancestor node to check whether this node became unbalanced'''       
        balance = self.getBalance(root) 
        
        '''If this node becomes unbalanced, then there are 4 cases'''
        
        '''Left Left Case'''
        if balance > 1 and data < root.left.data:
            print("Left Left Case : " + str(data))
            return self.rightRotate(root)
        
        '''Right Right Case'''
        if balance < -1 and data > root.right.data:
            print("Right Right Case : " + str(data))
            return self.leftRotate(root)
        
        '''Left Right Case'''
        if balance > 1 and data > root.left.data:
            print("Left Right Case : " + str(data))
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        '''Right Left Case'''
        if balance < -1 and data < root.right.data:
            print("Right Left Case : " + str(data))
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        '''return the (unchanged) node pointer '''
        return root

    '''inorder successor of a node '''
    def inorderSuccssor(self, root):

        while root.left is not None:
            root = root.left
        return root    
        
    
    ''' Delete a Node from BST '''
    def delete(self, root, data):
        
        '''1.  Perform the normal BST rotation'''
        if root is None:
            return root
        
        '''If the key to be deleted is smaller than the root's key, then it lies in left subtree'''
        if root.data > data:
            root.left = self.delete(root.left, data)
        
        elif root.data < data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None or root.right is None:
                temp = root.left if root.left is not None else root.right
                
                ''' no child case'''
                if temp is None:
                    root = None
                else:
                    '''One child case so Copy the contents of the non-empty child'''
                    root = temp
            else:
                '''node with two children: Get the inorder successor (smallest in the right subtree)'''  
                temp = self.inorderSuccssor(root.right)
                
                '''Copy the inorder successor's data to this node'''
                root.data = temp.data
                temp.data = None
        
        '''If the tree had only one node then return'''
        if root is None:
            return root
                
        '''2. Update height of this ancestor node'''
        root.height = max(self.nodeHeight(root.left), self.nodeHeight(root.right)) + 1
        
        '''3. Get the balance factor of this ancestor node to check whether this node became unbalanced'''       
        balance = self.getBalance(root) 
        
        '''If this node becomes unbalanced, then there are 4 cases'''
        
        '''Left Left Case'''
        if balance > 1 and data < root.left.data:
            print("Left Left Case : " + str(data))
            return self.rightRotate(root)
        
        '''Right Right Case'''
        if balance < -1 and data > root.right.data:
            print("Right Right Case : " + str(data))
            return self.leftRotate(root)
        
        '''Left Right Case'''
        if balance > 1 and data > root.left.data:
            print("Left Right Case : " + str(data))
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        '''Right Left Case'''
        if balance < -1 and data < root.right.data:
            print("Right Left Case : " + str(data))
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        '''return the (unchanged) node pointer '''
        return root
    
    ''' Preorder traversal , root,left,right'''    
    def preOrder(self, root):
        if root is None:
            return 0
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        

    

if __name__ == '__main__':
    root = Node(10)
    root = root.insert(root, 20)
    root = root.insert(root, 30)
    root = root.insert(root, 40)
    root = root.insert(root, 50)
    # root = root.insert(root, 25)
    root.preOrder(root)
    root = root.delete(root, 20)
    print("After delete")
    root.preOrder(root)
    root = root.delete(root, 30)
    print("After delete")
    root.preOrder(root)
    
    
