'''
Created on 24-Nov-2019

@author: anpradha

Implement *, – and / operations using only + arithmetic operator
Given two numbers, perform multiplication, subtraction and division operations on them, using ‘+’ arithmetic operator only.

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Operations can be performed as follows:

Subtraction :-  a - b = a + (-1)*b.
Multiplication :- a * b = a + a + a ... b times.
Division :- a / b =  continuously subtract b from a and 
                  count how many times we can do that.




'''

# Python3 code to illustrate *, -, / using  
# only  '+' arithmatic operator  

  
# Function to flip the sign using only "+"  
# operator (It is simple with '*' allowed.  
# We need to do a = (-1)*a  
def flipSign(a):  
  
    neg = 0;  
  
    # If sign is + ve turn it -ve  
    # and vice-versa  
    tmp = 1 if a < 0 else -1;  
    while (a != 0):  
        neg += tmp;  
        a += tmp;  
  
    return neg;  

  
# Check if a and b are of different signs  
def areDifferentSign(a, b): 
    return ((a < 0 and b > 0) or 
            (a > 0 and b < 0));  

  
# Function to subtract two numbers  
# by negating b and adding them  
def sub(a, b):  
  
    # Negating b  
    return a + flipSign(b);  

  
# Function to multiply a by b by  
# adding a to itself b times  
def mul(a, b):  
  
    # because algo is faster if b<a  
    if (a < b):  
        return mul(b, a);  
  
    # Adding a to itself b times  
    sum = 0;  
    for i in range(abs(b), 0, -1):  
        sum += a;  
  
    # Check if final sign must  
    # be -ve or + ve  
    if (b < 0):  
        sum = flipSign(sum);  
  
    return sum;  

  
# Function to divide a by b by counting  
# how many times 'b' can be subtracted  
# from 'a' before getting 0  
def division(a, b):  
  
    quotient = 0;  
  
    # Negating b to subtract from a  
    divisor = flipSign(abs(b));  
  
    # Subtracting divisor from dividend  
    # for dividend in range(abs(a), abs(divisor) + divisor, divisor):  
    #    quotient += 1;  
    
    x = abs(a)
    y = abs(b)    
    while x >= y:
        x = x + flipSign(abs(b))  
        quotient = quotient + 1;  
  
    # Check if a and b are of similar  
    # symbols or not  
    if (areDifferentSign(a, b)):  
        quotient = flipSign(quotient);  
    return quotient;  
  
# This code is contributed by mits 


if __name__ == '__main__':
    # Driver code  
    print("Subtraction is", sub(4, -2));  
    print("Product is", mul(-9, 6)); 
    a, b = 8, 2; 
    if(b): 
        print("Division is", division(a, b)); 
    else: 
        print("Exception :- Divide by 0");  
  
