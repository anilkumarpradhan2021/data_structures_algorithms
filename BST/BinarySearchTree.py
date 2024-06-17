'''
Created on 14-Aug-2016

@author: anpradha
'''
count = 0


class BST(object):
    '''
    classdocs
    '''

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def insert_bst(self, root, data):
        if root is None:
            root = BST(data)
            return
        
        temp = root
        if temp.data > data:
            if temp.left is None:
                temp.left = BST(data)
            else:
                self.insert_bst(temp.left, data)
        else:
            if temp.right is None:
                temp.right = BST(data)
            else:
                self.insert_bst(temp.right, data)            
        
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    "kth minimum is same as that of inorder with global count variable to count the node number"

    def kth_minimum_node(self, root , k):
        global count
        if root is None:
            return
        self.kth_minimum_node(root.left, k)
        count = count + 1 
        if count == k:
            print("Kth minimum Node : " + str(root.data))
        self.kth_minimum_node(root.right, k)

    def kth_minimum_node2(self, root , k, count):
        # global count
        if root is None:
            return
        self.kth_minimum_node2(root.left, k, count)
        count[0] = count[0] + 1 
        if count[0] == k:
            print("Kth minimum Node : " + str(root.data))
        self.kth_minimum_node2(root.right, k, count)

    "kth maximum is same as that of inorder with global count variable to count the node number "
    '''
    kth maximum is similar to kth minimum but inorder traversal will be reverse order , how to do ? easy .. 
    inplace of 
        left node, root node, right node
    try 
        right node, root node, left node
    '''

    def kth_maximum_node(self, root , k):
        global count
        if root is None:
            return
        self.kth_maximum_node(root.right, k)
        count = count + 1 
        if count == k:
            print("Kth maximum Node : " + str(root.data))
        self.kth_maximum_node(root.left, k)
        
    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    def minimum_node(self, root):
        if root is None :
            return None
        while(root.left is not None):
            root = root.left
            
        print("\nMinimum Is : " + str(root.data))    

    def maximum_node(self, root):
        if root is None :
            return None
        while(root.right is not None):
            root = root.right
            
        print("Maximum Is : " + str(root.data))    
    
    ''' Find distance from root to given node in a BST '''

    def distance_of_node(self, root, val, current_distance):
        if root is None :
            return 0
        if root.data == val:
            return current_distance + 1
        if root.data < val :
            return self.distance_of_node(root.right, val, current_distance + 1)
        else:
            return self.distance_of_node(root.left, val, current_distance + 1)

    def number_of_leaf_node(self, root):
        if root is None :
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            return self.number_of_leaf_node(root.left) + self.number_of_leaf_node(root.right)

    def print_all_leaf_node(self, root):
        if root is None :
            return 0
        if root.left == None and root.right == None:
            print(root.data, end=" ")
        self.print_all_leaf_node(root.left)
        self.print_all_leaf_node(root.right)

        
if __name__ == '__main__':
    root = BST(10)
    root.insert_bst(root, 6)
    root.insert_bst(root, 14)
    root.insert_bst(root, 4)
    root.insert_bst(root, 8)
    root.insert_bst(root, 12)
    root.insert_bst(root, 15)
    root.insert_bst(root, 16)

    root.inorder(root)
    # root.minimum_node(root)
    # root.maximum_node(root)
    # print("Distance from root to node : " + str(root.distance_of_node(root, 15, -1)))
    # root.kth_minimum_node2(root, 5, [0])
    # root.kth_maximum_node(root, 1)
    
    # # root.preorder(root)
    # print("Number of Leaf Node : " + str(root.number_of_leaf_node(root)))
    # print("Printing all leaf node : ")
    # root.print_all_leaf_node(root)
    
