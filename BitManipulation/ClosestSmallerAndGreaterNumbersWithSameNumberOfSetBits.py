'''
Created on 22-Nov-2019

@author: anpradha

Given a positive integer n, print the next smallest and the previous largest number that have the same number of 1 bits in their binary representation.

Examples :

Input : n = 5
Output : Closest Greater = 6
         Closest Smaller = 3
Note that 5, 6 and 3 have same number of 
set bits. 

Input : n = 11
Output : Closest Greater = 13
         Closest Smaller = 7



https://www.geeksforgeeks.org/closest-next-smaller-greater-numbers-number-set-bits/

'''
# Python 3 implementation of getNext with 
# same number of bits 1's is below 

  
# Main Function to find next smallest 
# number bigger than n 
def getNext(n): 
    print(bin(n))

    # Compute c0 and c1   
    c = n 
    c0 = 0
    c1 = 0
  
    while (((c & 1) == 0) and (c != 0)): 
        c0 += 1
        c >>= 1
      
    while ((c & 1) == 1): 
        c1 += 1
        c >>= 1
  
    # If there is no bigger number with  
    # the same no. of 1's 
    if (c0 + c1 == 31 or c0 + c1 == 0): 
        return -1
  
    # position of rightmost non-trailing zero 
    p = c0 + c1 
    print("p" , p, "c0" , c0, "c1" , c1)
  
    # Flip rightmost non-trailing zero 
    n = n | (1 << p) 
    print("n : " , n)
    print(bin(n))
  
    # Clear all bits to the right of p 
    n = n & ~((1 << p) - 1)  # or n = n & (~0 << p)

    # Insert (c1-1) ones on the right. 
    n = n | (1 << (c1 - 1)) - 1
  
    return n 
  

if __name__ == '__main__':
    number = 10
    number = 13948
    
    nextNumber = getNext(number)
    print(nextNumber)
    print(bin(nextNumber))
    
