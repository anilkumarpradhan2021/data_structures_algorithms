'''
Created on 28-Oct-2019

@author: anpradha
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_node(root):
    temp = root        
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()    


def add_node_to_end_of_list(root, val):
    newNode = Node(val)
    if root is None:
        root = newNode
        return root
    
    temp = root

    while temp.next is not None :
        temp = temp.next
    temp.next = newNode
    newNode.prev = temp


def insert_node_after_given_node(root, insertAfter, insertVal):
    newNode = Node(insertVal)
    
    ''' Assuming the node is present and root is not None'''
    
    if root is None:
        return -1
    
    temp = root

    ''' 1st find the node where we need to insert after '''
    while temp.next is not None  and temp.data != insertAfter:
        temp = temp.next
    
    newNode.next = temp.next    
    temp.next = newNode
    newNode.prev = temp 


def add_node_to_front_of_list(root, val):
    newNode = Node(val)
    newNode.next = root
    root = newNode
    return root

    
def delet_node(root, val):
    if root is None:
        return -1
    else:
        temp = root
        previous = temp
        while temp and temp.data != val:
            previous = temp
            temp = temp.next
        
        if temp == root:
            print("its a root node")
            root = root.next
            root.prev = None
        else:
            previous.next = temp.next
            temp.next.prev = previous
            del temp   
        return root     


if __name__ == '__main__':
    root = None
    root = add_node_to_end_of_list(root, 10)
    add_node_to_end_of_list(root, 20)
    add_node_to_end_of_list(root, 30)
    add_node_to_end_of_list(root, 40)
    print_node(root)
    root = delet_node(root, 20)
    print_node(root)
    root = delet_node(root, 10)
    print_node(root)
    root = add_node_to_front_of_list(root, 100)
    print_node(root)
    insert_node_after_given_node(root, 100, 200)
    print_node(root)
    
