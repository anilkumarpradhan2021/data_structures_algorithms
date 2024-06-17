
# Python3 program to Select a  
# Random Node from a tree 
from random import randint 

  
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.children = 0
        self.left = None
        self.right = None

  
# This is used to fill children counts.  
def getElements(root):  
  
    if root == None:  
        return 0
          
    return (getElements(root.left) + 
            getElements(root.right) + 1)  

  
# Inserts Children count for each node  
def insertChildrenCount(root):  
  
    if root == None: 
        return
  
    root.children = getElements(root) - 1
    insertChildrenCount(root.left)  
    insertChildrenCount(root.right)  

  
# Returns number of children for root  
def children(root): 
  
    if root == None:  
        return 0
    return root.children + 1

  
# Helper Function to return a random node  
def randomNodeUtil(root, count):  
  
    if root == None:  
        return 0
  

    if count == children(root.left):
        return root.data  
  
    if count < children(root.left):  
        return randomNodeUtil(root.left, count)  
  
    return randomNodeUtil(root.right,
            count - children(root.left) - 1)  

  
# Returns Random node  
def randomNode(root):  
  
    count = randint(0, root.children) 
    return randomNodeUtil(root, count) 

  
# Driver Code 
if __name__ == "__main__": 
  
    # Creating Above Tree  
    root = Node(10)  
    root.left = Node(20)  
    root.right = Node(30)  
    root.left.right = Node(40)  
    root.left.right = Node(50)  
    root.right.left = Node(60)  
    root.right.right = Node(70)  
  
    insertChildrenCount(root)  
  
    print("A Random Node From Tree :",
           randomNode(root)) 
  
# This code is contributed by Rituraj Jain 
