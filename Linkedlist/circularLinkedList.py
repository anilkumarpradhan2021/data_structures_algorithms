'''
Created on 28-Oct-2019

@author: anpradha

https://www.geeksforgeeks.org/circular-singly-linked-list-insertion/

we have consider last node 
so start node is last.next

'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    
def insert_empty_list(last, val):
    if last is None:
        newNode = Node(val)
        last = newNode
        last.next = last
        return last
    else:
        return last


def addBegin(last, val):
    newNode = Node(val)
    if last is None:
        return insert_empty_list(last, val)
    else:
        newNode.next = last.next
        last.next = newNode
    return last


def addEnd(last, val):
    if last is None:
        return insert_empty_list(last, val)
    else:
        newNode = Node(val)
        newNode.next = last.next
        last.next = newNode
        last = newNode
    return last


def addAfter(last, insertAfterValue, value):
    if last is None:
        return None
    temp = last.next
    newNode = Node(value)
    while temp:
        if temp.data == insertAfterValue:
            newNode.next = temp.next
            temp.next = newNode
            if temp == last:
                last = newNode
                return last
            else:
                return last
        
        if temp == last:
            print("Element not found to  insert after")
            break
        
        temp = temp.next
             

def traversal(last):
    temp = last.next
    while temp != last:
        print(temp.data, end=" ")
        temp = temp.next
    print(last.data)            
    print()                


if __name__ == '__main__':
    last = None
    last = insert_empty_list(last, 10)
    traversal(last)
    last = addBegin(last, 30)
    traversal(last)
    last = addEnd(last, 20)
    traversal(last)
    last = addAfter(last, 10, 11)
    traversal(last)
    last = addAfter(last, 20, 21)
    traversal(last)
    print("last : ", last.data)
