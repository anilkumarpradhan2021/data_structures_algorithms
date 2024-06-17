'''
Created on 11-Aug-2019

@author: anpradha


Program to find HCF (Highest Common Factor) of 2 Numbers
HCF (Highest Common Factor) or GCD (Greatest Common Divisor) of two numbers is the largest number that divides both of them.

GCD

For example GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.

An efficient solution is to use Euclidean algorithm which is the main algorithm used for this purpose. 
The idea is, GCD of two numbers doesn’t change if smaller number is subtracted from a bigger number.

'''
# Recursive function to return gcd of a and b 
def gcd2(a,b): 
      
    # Everything divides 0  
    if (a == 0 or b == 0): 
            False
    # base case 
    if (a == b): 
        return a 
  
    # a is greater 
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a) 

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    a , b = 30, 36
    a , b = 36 , 60
            
    print("GCD or HCD Of {a} and  {b} is : ".format(a=a, b=b), gcd(a, b))
    
