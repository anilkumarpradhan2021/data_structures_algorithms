'''
Created on 24-Sep-2016

@author: anpradha


Problem Statement:
We are given a list of prices of a stock for N number of days. We need to find stock span for each day.
Span is defined as number of consecutive days before the given day where the price of stock was less than or 
equal to price at given day. For example, {100, 60,70,65, 80, 85} span for each day will be {1, 1, 2, 1, 4, 5}.


For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, 
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}



Algorithm to detect stock span

1. Initialize span of day 1 as 1.
2. Put day 1 on to stack. 
3. For all days starting from day 2, repeat following steps. 
   3.1 If price of stock on day at top of stack is less than price of stock on current day, Pop the index from stack. 
   3.2 If price of stock on the day on top of stack is greater than price of stock on current day, calculate span as current day - day at top of stack. 
   3.3 Push current day index on to stack.
   
'''

if __name__ == '__main__':
    stock = [10, 4, 5, 90, 120, 80]
    
    ''' Create a stack and push index of fist element to it '''
    stock_stack = []
    stock_stack.append(0)
    
    ''' Span value of first element is always 1 and others default value 1 '''
    span = [1 for _ in range(len(stock))]
    
    for i in range(1, len(stock)):
        '''  Pop elements from stack while stack is not empty and top of stack is smaller than price[i]  note : stock_stack[-1] is TOP '''
        while len(stock_stack) > 0 and stock[stock_stack[-1]] <= stock[i]:
            stock_stack.pop()
            
        ''' if stack is empty then then price[i] is greater than all elements on left of it, i.e. price[0], price[1], ..price[i-1].'''    
        if len(stock_stack) <= 0:
            span[i] = i + 1
        else:  
            span[i] = i - stock_stack[-1]  # stock_stack[-1] is TOP of stack
        
        ''' Push this element to stack'''          
        stock_stack.append(i)

    print(span)
