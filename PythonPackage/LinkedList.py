'''
Created on 05-May-2016

@author: anpradha
'''

class Node(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.data = None
        self.next = None
    
    # method for setting data
    def setData(self, data):
        self.data = data

    # method for get the data
    def getData(self):
        return self.data
    
    # method for set next pointer
    def setNext(self, next):
        self.next = next
        
    # method for get next pointer location    
    def getNext(self):
        return self.next
    
    def getListLength(self):
        temp = self.head
        counter = 0 
        while(temp != None):
            counter = counter + 1 
            temp = temp.getNext()
        return counter
        
    # method to check if next element is present or not
    def hasNext(self):
        return self.next != None    
                
    def print(self):
        current = self.head
        while(current != None):
            print(current.data)
            current = current.getNext()
            
    def insert_at_end(self, data):
        temp = Node()     
        temp.setData(data)
        temp.setNext(None)
        
        # now travel the list
        current = self.head
        while(current.getNext() != None):
            current = current.getNext()
        current.setNext(temp)

    def insert_at_begining(self, data):
        temp = Node()     
        temp.setData(data)
        # If no node present
        if self.head == None:
            self.head = temp
        else:
            temp.setNext(self.head)
            self.head = temp
            
    def insert_position(self, data, position):
        temp = Node()     
        temp.setData(data)
        # If no node present
        if position == 0:
            self.insert_at_begining(data)
        if position == self.getListLength():
            self.insert_at_end(data)    
        if position <= self.getListLength():
            print()
            count = 0
            temp = self.head 
            while(count < position):
                temp = temp.getNext()
                count = count + 1
            #create a new node
            newNode = Node()
            newNode.setData(data)
            newNode.setNext(temp.getNext())
            temp.setNext(newNode)    
        else:
            print("invalid position")    

    def delete_from_begining(self):
        if self.getListLength() == 0:
            print("empty list")
        else:    
            temp = self.head
            self.head = self.head.getNext()

    def delete_from_last(self):
        if self.getListLength() == 0:
            print("empty list")
        else:    
            temp = self.head
            previous_node = self.head 
            while(temp.getNext() !=None):
                previous_node = temp
                temp = temp.getNext()
            previous_node.setNext(None)
            
            
            