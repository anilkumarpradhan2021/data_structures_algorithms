'''
Created on 05-Oct-2019

@author: anpradha

Print all combinations of balanced parentheses

Write a function to generate all possible n pairs of balanced parentheses.

Examples:

Input : n=1
Output: {}

Input : n=2
Output: 
{}{}
{{}}



'''

# Wrapper over _printParenthesis() 
def printParenthesis(str, n): 
    if(n > 0): 
        _printParenthesis(str, 0,
                          n, 0, 0); 
    return; 

  
def _printParenthesis(str, pos, n,
                      open, close): 
      
    if(close == n): 
        print(str)
        return; 
    else: 
        if(open > close): 
            str[pos] = '}'; 
            _printParenthesis(str, pos + 1, n,
                              open, close + 1); 
        if(open < n): 
            str[pos] = '{'; 
            _printParenthesis(str, pos + 1, n,
                              open + 1, close); 
  
# Driver Code 

if __name__ == '__main__':
    n = 2; 
    str = [""] * 2 * n;  # this is the maximum length of a valid o/p 
    printParenthesis(str, n); 
