'''
Created on 28-Oct-2019

@author: anpradha

https://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/

Convert a given Binary Tree to Doubly Linked List | Set 3
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. 
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. 
The order of nodes in DLL must be same as Inorder of the given Binary Tree. 
The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

Time Complexity: The above program does a simple inorder traversal, so time complexity is O(n) where n is the number of nodes in given binary tree.

'''

from queue import Queue


class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertBT(root, data):
    if root is None:
        return Node(data)
    else:
        q = Queue()
        q.put(root)
        
        while True:
            node = q.get()
            
            if node.left is None:
                node.left = Node(data)
                break
            else:
                q.put(node.left)
                    
            if node.right is None:
                node.right = Node(data)
                break
            else:
                q.put(node.right)


def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.data , end=" ")
    inOrder(root.right)

head = None
previous = None


def BTtoDoubleLinkListInOrder(root):
    global head
    global previous

    if root is None:
        return None
    
    # left
    BTtoDoubleLinkListInOrder(root.left)
    
    ''' for very 1st time start from left most element'''
    if previous is None:
        head = root
        previous = head
    else:
        previous.right = root
        root.left = previous
    
    previous = root    

    # right
    BTtoDoubleLinkListInOrder(root.right)


def travelDoubleList(head):
    if head is None:
        return
    temp = head
    while temp is not None:
        print(temp.data , end=" ")
        temp= temp.right
    print()    

                
if __name__ == '__main__':
    root = None
    root = insertBT(root, 10)
    inOrder(root)
    print()
    insertBT(root, 20)
    insertBT(root, 30)
    insertBT(root, 40)
    inOrder(root)
    print()
    BTtoDoubleLinkListInOrder(root)
    print(head)
    travelDoubleList(head)
    
