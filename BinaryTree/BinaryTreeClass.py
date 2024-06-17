'''
Created on 28-Jul-2016

@author: anpradha
'''
from queue import Queue

class MyBinary(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
    
    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right
    
    '''
       
    '''
            
    def insertData(self, root, data):
        newNode = MyBinary(data)
        if root is None:
            root = newNode
            return root

        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node.getLeft() is not None:
                q.put(node.getLeft())
            else:
                node.setLeft(newNode)
                return root
                
            if node.getRight() is not None:
                q.put(node.getRight())
            else:
                node.setRight(newNode)
                return root    
    
    
    
    ''' 1 + left + right '''
    def number_of_element(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.number_of_element(root.getLeft()) + self.number_of_element(root.getRight())

    ''' 1 + left data + right data '''
    def sum_of_all_element(self, root):
        if root is None:
            return 0
        else:
            return root.getData() + self.sum_of_all_element(root.getLeft()) + self.sum_of_all_element(root.getRight())
    
    ''' print level - 0 , level -1 ....
     For level order traversal use Queue '''    
    def levelOrderTravel(self, root):
        if (root is not None):
            q = Queue()
            q.put(root)
                     
            while(not q.empty()):
                node = q.get()
                print(node.getData() ,end = " ")
                
                if (node.getLeft() is not None):
                    q.put(node.getLeft())
                
                if (node.getRight() is not None):
                    q.put(node.getRight())  
        else:
            print("Binary tree Is empty")                  

    '''' reverse Level Traversal Means print Level n, Level n-1 ,Level n-2 ... '''

    def reverLevelOrderTravel(self, root):
        if (root is not None):
            q = Queue()
            q.put(root)
            stack = []
            while(not q.empty()):
                node = q.get()
                
                if (node.getRight() is not None):
                    q.put(node.getRight())

                if (node.getLeft() is not None):
                    q.put(node.getLeft())

                stack.append(node)    
          
        else:
            print("Binary tree Is empty") 
        
        for i in range(len(stack)):
            node = stack.pop()
            print(node.getData(),end=" ")

    ''' For Delete a Tree we need to use Post Order Traversal like Left,Right and then Root '''
    def deleteBinaryTree(self, root):
        if root == None:
            return 
        self.deleteBinaryTree(root.getLeft())
        self.deleteBinaryTree(root.getRight())
        del root


    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.getLeft()), self.maxDepth(root.getRight())) + 1         

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
            if node.getLeft() is not None:
                q.append([node.getLeft() , max_depth + 1])

            if node.getRight() is not None:
                q.append([node.getRight() , max_depth + 1])
        return max_depth       

    '''Deepest Node is nothing but the last node of the tree'''
    def deepestNode(self, root):
        if root == None:
            print("Empty")
        
        q = Queue()
        q.put(root)
        node = None
        while not q.empty():
            node = q.get()

            if node.getLeft() is not None:
                q.put(node.getLeft())
                    
            if node.getRight() is not None:
                q.put(node.getRight())
        print(node.getData())  

    '''Print all path from root to all leaf node'''
    def printAllPath(self, root, current_path, paths):
        if root is None: 
            return 0
        # current_path = str(current_path) + " -> " + str(root.data)
        current_path = current_path + [root.data]
        print("current_path : " + str(current_path))
        
        if root.getLeft() is None and root.getRight() is None:
            paths.append(current_path)
        if root.getLeft() is not None:
            self.printAllPath(root.getLeft(), current_path, paths)
        if root.getRight() is not None:
            self.printAllPath(root.getRight(), current_path, paths)
                
    def printPath(self, root):
        paths = []
        self.printAllPath(root, [], paths)
        for counter in range(len(paths)):
            print(paths[counter])

    def totalSumFromrootToLeafForAllPath(self, root):
        paths = []
        self.printAllPath(root, [], paths)
        for counter in range(len(paths)):
            print(paths[counter])
            sum = 0 
            for c in range(len(paths[counter])):
                sum = sum * 10 + paths[counter][c]
            print(sum)    
    
    def diameterOfTree(self, root):
        if root is None:
            return 0;
        leftHeight = self.maxDepth(root.getLeft())
        rightHeight = self.maxDepth(root.getRight())
        lDiameter = self.diameterOfTree(root.getLeft())
        rDiameter = self.diameterOfTree(root.getRight())
        return max((leftHeight + rightHeight + 1), max(lDiameter , rDiameter)) 
         
    def levelhavingMaximumSum(self, root):
        if root is None:
            return 0;
        q = Queue()
        q.put(root)
        q.put(None)
        max_sum = 0 
        current_sum = 0
        level = 0
        max_level = 0 
        while not q.empty():
            node = q.get()
            if node is None:
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_level = level
                current_sum = 0     
                if not q.empty():
                    level = level + 1
                    q.put(None)
            else:
                current_sum = current_sum + node.getData()
                if node.getLeft() is not None:
                    q.put(node.getLeft())
                if node.getRight() is not None:
                    q.put(node.getRight())
        return max_level       
    
    def existanceOfGivenSum(self, root, val, current_path, paths):
        if root is None :
            return False
        
        current_path = current_path + [root.getData()]
        if root.getData() == val:
            paths.append(current_path)
            return True
        
        if root.getLeft() is not None: 
            left = self.existanceOfGivenSum(root.getLeft(), val - root.getData() , current_path, paths) 
        else:
            left = False        
        
        if root.getRight() is not None:    
            right = self.existanceOfGivenSum(root.getRight(), val - root.getData(), current_path, paths) 
        else:
            right = False    
        
        return left or right    

    def ancensterOfGivenNode(self, root, val):
        if root is None :
            return False
        
        if root.getData() == val:
            return True
        
        if self.ancensterOfGivenNode(root.getLeft(), val)  or self.ancensterOfGivenNode(root.getRight(), val): 
                print(root.getData())
                return True
        
        return False  
    
    def printExistanceOfGivenSum(self, root, val):
        current_path = []
        paths = []
        print("Path Exits or not : " + str(self.existanceOfGivenSum(root, val, current_path, paths)))
        print("Path exists : " + str(paths))

                          
if __name__ == '__main__':
    b = MyBinary(1)
    root = b.insertData(b, 2)
    b.insertData(root, 3)
    b.insertData(root, 4)
    b.insertData(root, 5)
    b.insertData(root, 6)
    b.insertData(root, 7)
    print("Level order Traversal")
    b.levelOrderTravel(root)
    print()
    print("Reverse Level order Traversal")
    b.reverLevelOrderTravel(root)
    print()
    b.deleteBinaryTree(root)
    print("number of element : " + str(b.number_of_element(root)))
    print("Maximum Depth : " + str(b.maxDepth(root)))
    print("Maximum Depth : " + str(b.maxDepthWithoutRecurssion(root)))
    print("Deepest Node ")
    b.deepestNode(root)
    b.printPath(root)
    b.totalSumFromrootToLeafForAllPath(root)
    print("Max Sum of  a level : " + str(b.levelhavingMaximumSum(root)))
    b.printExistanceOfGivenSum(root, 7)
    print("Ancenster of a given node :")
    b.ancensterOfGivenNode(root, 7)  
    print(b.sum_of_all_element(root))  
        
        
