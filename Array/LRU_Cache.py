'''
Created on 14-Nov-2019

@author: anpradha

LRU (Remove Least Recently Used item from Cache)
LRU Cache Implementation in Python w/ Explanation

The basic idea behind the LRU cache is that we want to query our queue in O(1)/constant time. We also want to insert into the cache in O(1) time. 
Therefore, get, set should always run in constant time. This is the reason we use a hash map or a static array (of a given size with an appropriate hash function) to retrieve items in constant time.


We are given total possible page numbers that can be referred. 
We are also given cache (or memory) size (Number of page frames that cache can hold at a time). 
The LRU caching scheme is to remove the least recently used frame when the cache is full 
and a new page is referenced which is not there in cache. 


We use two data structures to implement an LRU Cache. 
 

1. Queue which is implemented using a doubly linked list. 
The maximum size of the queue will be equal to the total number of frames available (cache size).
The most recently used pages will be near front end and least recently pages will be near the rear end. 
 
2. A Hash with page number as key and address of the corresponding queue node as value.

'''
from platform import node


class Node():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    
MAX = 1


class LRU():

    def __init__(self, capacity=0):
        self.d = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
    
    def getKey(self, key):
        if key in self.d:
            node = self.d[key]
            # remove the node
            self.remove(node)
            # move this node to front 
            self.set_to_head(node)    
            return node
        else:
            return -1

    def setKey(self, key, value):
        if key not in self.d:
            node = Node(key, value)
            print("capacity : " , self.capacity)
            if self.capacity >= MAX:
                print("max capacity reached so delete the least used element ")
                del self.d[self.tail.key]
                self.remove(self.tail)
            self.set_to_head(node)
            self.d[key] = node
            self.capacity = self.capacity + 1
        else:
            node = self.d[key]
            self.remove(node)
            self.node.value = value   
            self.set_to_head(node)  
        
        print("Key added Successful " , key)       
    
    def set_to_head(self, node):
        if not self.head :
            self.head = node
            self.tail = node
        else:    
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
    
    def remove(self, node):
        
        ''' if node is head node'''
        if self.head == node:
            ''' if we have only one element that is head and tail'''
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                #self.head.next = self.head.prev
                self.head = self.head.next
                self.head.prev = None
        
        elif self.tail == node:
            self.tail.prev.next = None
            self.tail = self.tail.prev        
                
        else:
            node.next.pre = node.prev
            node.prev.next = node.next        
        
    def printAll(self):
        temp = self.head
        while temp:
            print(temp.value , end=" ")
            temp = temp.next  
        print()    

                   
if __name__ == '__main__':
    cache = LRU()
    print("No key trying to get a key")
    print(cache.getKey(1))
    cache.setKey(1, 1)
    cache.setKey(2, 2)
    cache.setKey(3, 3)
    cache.printAll()
    print("Get key 1")
    cache.getKey(1)
    cache.printAll()
    print("Add a element 4 after capacity ")
    cache.setKey(4, 4)
    cache.printAll()
