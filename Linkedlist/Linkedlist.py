'''
Created on 22-Oct-2016

@author: anpradha
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_node(root, val):
    if root is None:
        root = Node(val)
        return root
    temp = root
    
    while temp.next is not None :
        temp = temp.next
    temp.next = Node(val)
    
def print_node(root):
    temp = root        
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()    

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
        else:
            previous.next = temp.next
            del temp   
        return root     
        
    
if __name__ == '__main__':
    root = None
    root = add_node(root, 10)
    add_node(root, 20)
    add_node(root, 30)
    add_node(root, 40)
    print_node(root)
    root = delet_node(root, 20)
    print_node(root)
    root = delet_node(root, 10)
    print_node(root)
