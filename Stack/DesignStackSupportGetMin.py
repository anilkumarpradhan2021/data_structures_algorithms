'''
Created on 21-Sep-2019

@author: anpradha

Design a stack that supports getMin() in O(1) time and O(1) extra space
Question: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data structure and no other data structure like arrays, list, .. etc.

Example:

Consider the following SpecialStack
16  --> TOP
15
29
19
18

When getMin() is called it should return 15, 
which is the minimum element in the current stack. 

If we do pop two times on stack, the stack becomes
29  --> TOP
19
18

When getMin() is called, it should return 18 
which is the minimum in the current stack.


https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/


Same Concept for getMax()
https://www.geeksforgeeks.org/find-maximum-in-a-stack-in-o1-time-and-o1-extra-space/
s

'''


class Stack():

    def __init__(self):
        self.min_val = float("inf")
        self.stack_list = []

    def push(self, ele):
        if len(self.stack_list) == 0:
            self.min_val = ele
            self.stack_list.append(ele)
        elif ele < self.min_val:
            self.stack_list.append(2 * ele - self.min_val)
            self.min_val = ele
        else:
            self.stack_list.append(ele)    
            
    def pop(self):
        popped_ele = self.stack_list.pop()
        if popped_ele < self.min_val:
            print("popped element: ", self.min_val)
            self.min_val = 2 * self.min_val - popped_ele
        else:
            print("popped element: " , popped_ele)    

    def getMin(self):
        return "Min :  " + str(self.min_val)


if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(5)
    print(s.getMin())
    s.push(2)
    s.push(1)
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    
