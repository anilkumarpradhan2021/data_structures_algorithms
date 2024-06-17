'''
Created on 25-Sep-2019

@author: anpradha

Expression Evaluation
Evaluate an expression represented by a String. Expression can contain parentheses, you can assume parentheses are well-matched. 
For simplicity, you can assume only binary operations allowed are +, -, *, and /. Arithmetic Expressions can be written in one of three forms:

Infix Notation: Operators are written between the operands they operate on, e.g. 3 + 4 .

Prefix Notation: Operators are written before the operands, e.g + 3 4

Postfix Notation: Operators are written after operands.




1. While there are still tokens to be read in,
   1.1 Get the next token.
   1.2 If the token is:
       1.2.1 A number: push it onto the value stack.
       1.2.2 A variable: get its value, and push onto the value stack.
       1.2.3 A left parenthesis: push it onto the operator stack.
       1.2.4 A right parenthesis:
         1 While the thing on top of the operator stack is not a 
           left parenthesis,
             1 Pop the operator from the operator stack.
             2 Pop the value stack twice, getting two operands.
             3 Apply the operator to the operands, in the correct order.
             4 Push the result onto the value stack.
         2 Pop the left parenthesis from the operator stack, and discard it.
       1.2.5 An operator (call it thisOp):
         1 While the operator stack is not empty, and the top thing on the
           operator stack has the same or greater precedence as thisOp,
           1 Pop the operator from the operator stack.
           2 Pop the value stack twice, getting two operands.
           3 Apply the operator to the operands, in the correct order.
           4 Push the result onto the value stack.
         2 Push thisOp onto the operator stack.
2. While the operator stack is not empty,
    1 Pop the operator from the operator stack.
    2 Pop the value stack twice, getting two operands.
    3 Apply the operator to the operands, in the correct order.
    4 Push the result onto the value stack.
3. At this point the operator stack should be empty, and the value
   stack should have only one value in it, which is the final result.
   
   Time Complexity: O(n)
   Space Complexity: O(n)


   
'''


def evaluateExpression(str):
    operator_stack = []
    value_stack = []
    
    precedence_array = {"+": 1, "-": 1 , "*": 2 , "/": 3}
    # read one by one char and put it to value if digit ele put it to operator
    i = 0
    while i < len(str):

        if str[i].isdigit():
            digit_val = 0
            
            while i < len(str) and str[i].isdigit():
                digit_val = digit_val * 10 + int(str[i])
                i = i + 1
                
            value_stack.append(digit_val)
            i = i - 1
        
        # operator stack
        else:
            # if stack is not empty
            if len(operator_stack) > 0 :
                operator = operator_stack[-1]
                
                # if top operator precedence is same or more than new operator
                if precedence_array[operator] >= precedence_array[str[i]]:
                    # pop 2 value from value and execute the operator and push the value back to Value Stack
                    val1 = value_stack.pop()
                    val2 = value_stack.pop()
                    evaluated_value = evalute_operator(val1, val2, operator)
                    value_stack.append(evaluated_value)
                    
                    # remove the operator from operator stack
                    operator_stack.pop()
                    
                    # add the new operator
                    operator_stack.append(str[i])
                
                # if the new operator precedence is more then add it .
                else:
                    # add the new operator
                    operator_stack.append(str[i])
            
            else:
                # add the new operator
                operator_stack.append(str[i])
        i = i + 1
    # 
    while len(operator_stack) > 0:
        # pop 2 value from value and execute the operator and push the value back to Value Stack
        val1 = value_stack.pop()
        val2 = value_stack.pop()
        operator = operator_stack.pop()
        evaluated_value = evalute_operator(val1, val2, operator)
        value_stack.append(evaluated_value)
    
    print(value_stack)    
        

def evalute_operator(val1, val2, operator):
    if operator == "*":
        return val1 * val2
    if operator == "/":
        return val1 / val2
    if operator == "+":
        return val1 + val2
    if operator == "-":
        return val1 - val2

          
if __name__ == '__main__':
    str = "10+2*6"
    # str = "100*2+12/14" 
    evaluateExpression(str)
