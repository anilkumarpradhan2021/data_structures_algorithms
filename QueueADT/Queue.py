'''
Created on 03-Jul-2016

@author: anpradha
'''

class MyClass(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.size = 0;
        self.head = None
        self.last = None
        
    def printQueue(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next
            
    def enQueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size = self.size + 1
    
    def deQueue(self):
        if self.size == 0:
            print("Queue is empty")
        else:
            temp = self.head
            self.head = self.head.next
            print(temp.data)
            self.size = self.size - 1  
          
class Node(object):
    
    def __init__(self, data):
        self.next = None
        self.data = data
    
if __name__ == '__main__':
    queue = MyClass()
    queue.enQueue(1)
    queue.enQueue(2)
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()
    
