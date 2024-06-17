'''
Created on 29-Jul-2016

@author: anpradha
'''

class Stack(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.items = []
    
    def push(self,data):
        self.items.append(data) 
        
    def pop(self):
        self.items.pop()
        
if __name__ == '__main__':
    s  = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())
              



    