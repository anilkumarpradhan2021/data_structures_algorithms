'''
Created on 28-Oct-2019

@author: anpradha

https://www.geeksforgeeks.org/convert-a-binary-tree-to-a-circular-doubly-link-list/



'''


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def traversalCircularDoubleLinkedList(root):
    if root is None:
        return
    temp = root
    while temp:
        print(temp.data, end="->")
        temp = temp.next
        
        if temp == root:
            break

    print()


def concatenate(leftlist, rightList):
    
    if leftlist is None:
        return rightList
    if rightList is None:
        return leftlist
    
    ''' last node of left'''
    leftLast = leftlist.prev

    ''' last node of right'''
    rightLast = rightList.prev
    
    leftLast.next = rightList
    rightList.prev = leftLast
    
    
    '''
        # prev of first node points to  
        # the last node in the list  
    
    '''
    leftlist.prev = rightLast
    
    '''     # next of last node refers to  
            # the first node of the List  
    '''
    rightLast.next = leftlist
    
       
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    '''Point to head of left list'''
    left = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node1
    node1.prev = node3    
    traversalCircularDoubleLinkedList(left)
    print(left.data)

    node1 = Node(4)
    node2 = Node(5)
    node3 = Node(6)

    '''Point to head of right list'''
    right = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node1
    node1.prev = node3    
    traversalCircularDoubleLinkedList(right)
    print(right.data)
    
    concatenate(left, right)
    traversalCircularDoubleLinkedList(left)
    
