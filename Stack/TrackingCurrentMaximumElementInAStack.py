'''
Created on 21-Sep-2019

@author: anpradha

Tracking current Maximum Element in a Stack
Given a Stack, keep track of the maximum value in it. The maximum value may be the top element of the stack, 
but once a new element is pushed or an element is pop from the stack, the maximum element will be now from the rest of the elements.

Examples:

Input : 4 19 7 14 20
Output : Max Values in stack are 
         4 19 19 19 20

Input : 40 19 7 14 20 5
Output :  Max Values in stack are 
         40 40 40 40 40 40
         
Method 2 (Efficient): An efficient approach would be to maintain an auxiliary stack while pushing element in the main stack. This auxiliary stack will keep track of the maximum element.
Below is the step by step algorithm to do this:

Create an auxiliary stack, say ‘trackStack’ to keep the track of maximum element
Push the first element to both mainStack and the trackStack.
Now from the second element, push the element to the main stack. Compare the element with the top element of the track stack,
if the current element is greater than top of trackStack then push the current element to trackStack otherwise push the top element of trackStack again into it.
If we pop an element from the main stack, then pop an element from the trackStack as well.
Now to compute the maximum of the main stack at any point, we can simply print the top element of Track stack.
Step by step explanation :
Suppose the elements are pushed on to the stack in the order {4, 2, 14, 1, 18}
Step 1 : Push 4, Current max : 4
Step 2 : Push 2, Current max : 4
Step 3 : Push 14, Current max : 14
Step 4 : Push 1, Current max : 14
Step 5 : Push 18, Current max : 18
Step 6 : Pop 18, Current max : 14         
         
         
'''


class StackWithTrackMax():

    def __init__(self):
        self.actual_stack = []
        self.aux_stack = []
    
    def push(self, elem):
        if len(self.actual_stack) == 0:
            self.actual_stack.append(elem)
            self.aux_stack.append(elem)
        else:
            self.actual_stack.append(elem)
            top_element = self.aux_stack[-1]
            if top_element < elem:
                self.aux_stack.append(elem)
            else:
                self.aux_stack.append(top_element)
    
    def pop(self):
        print(self.actual_stack.pop())
        print(self.aux_stack.pop())                
    
    def getMax(self):
        return self.aux_stack[-1]    


if __name__ == '__main__':
    s = StackWithTrackMax()
    s.push(20)
    print("Max : " , s.getMax())

    s.push(10)
    print("Max : " , s.getMax())

    s.push(50)
    print("Max : " , s.getMax())
    
    
