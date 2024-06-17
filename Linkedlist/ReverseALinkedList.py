'''
Created on 22-Nov-2019

@author: anpradha

Reverse a linked list
Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing links between nodes.

Examples:

Input: Head of following linked list
1->2->3->4->NULL
Output: Linked list should be changed to,
4->3->2->1->NULL

Input: Head of following linked list
1->2->3->4->5->NULL
Output: Linked list should be changed to,
5->4->3->2->1->NULL




'''
# Python program to reverse a linked list  
# Time Complexity : O(n) 
# Space Complexity : O(1) 

  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None

  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to reverse the linked list 
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next_node = current.next
            current.next = prev 
            prev = current 
            current = next_node
        self.head = prev 
          
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next
  

if __name__ == '__main__':
    # Driver program to test above functions 
    llist = LinkedList() 
    llist.push(20) 
    llist.push(4) 
    llist.push(15) 
    llist.push(85) 
      
    print("Given Linked List")
    llist.printList() 
    llist.reverse() 
    print("\nReversed Linked List")
    llist.printList()
