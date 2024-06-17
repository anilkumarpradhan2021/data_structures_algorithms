'''
Created on 21-Sep-2019

@author: anpradha

Sort a stack using a temporary stack
Given a stack of integers, sort it in ascending order using another temporary stack.

Examples:

Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
We follow this algorithm.

Create a temporary stack say tmpStack.
While input stack is NOT empty do this:
Pop an element from input stack call it temp
while temporary stack is NOT empty and top of temporary stack is greater than temp,
pop from temporary stack and push it to the input stack
push temp in temporary stack
The sorted numbers are in tmpStack


https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/

'''


def sortStack(stack1):
    stack2 = []
    
    while len(stack1) > 0:
        s1 = stack1.pop()
        
        while len(stack2) > 0 and stack2[-1] > s1:
            stack1.append(stack2.pop())
        
        stack2.append(s1)      
    print(stack2)          
        
    
if __name__ == '__main__':
    stack1 = [34, 3, 31, 98, 92, 23]
    print(stack1)
    sortStack(stack1)
    
