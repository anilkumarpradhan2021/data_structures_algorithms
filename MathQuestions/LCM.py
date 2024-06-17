'''
Created on 11-Aug-2019

@author: anpradha

LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers.
For example LCM of 15 and 20 is 60 and LCM of 5 and 7 is 35.

An efficient solution is based on below formula for LCM of two numbers ‘a’ and ‘b’.

 a x b = LCM(a, b) * GCD (a, b)
 
 LCM(a, b) = (a x b) / GCD(a, b) 
 
 
'''


# Recursive function to return gcd of a and b 
def gcd(a, b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 

  
# Function to return LCM of two numbers 
def lcm(a, b): 
    return (a * b) / gcd(a, b)


if __name__ == '__main__':
    a = 15 
    b = 20
    print('LCM of', a, 'and', b, 'is', lcm(a, b)) 
