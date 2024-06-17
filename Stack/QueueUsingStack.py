'''
Created on 21-Sep-2019

@author: anpradha
'''


class QueueUsingStack():

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, ele):
        self.stack1.append(ele)

    def dequeue(self):
        # check if stack2 is empty , if yes , then check for stack 1 and move all element from stack1 to stack2 and pop
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            raise Exception("Queue is empty")
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())    
            element = self.stack2.pop()
        else:
            element = self.stack2.pop()
        print(element)    


if __name__ == '__main__':
    q = QueueUsingStack()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    
