'''
Created on 25-Sep-2019

@author: anpradha

Find longest sequence of 1’s in binary representation with one flip
Give an integer n. We can flip exactly one bit. Write code to find the length of the longest sequence of 1 s you could create.

Examples:

Input : 1775         
Output : 8 
Binary representation of 1775 is 11011101111.
After flipping the highlighted bit, we get 
consecutive 8 bits. 11011111111.

Input : 12         
Output : 3 

Input : 15
Output : 5

Input : 71
Output: 4

Binary representation of 71 is 1000111.
After flipping the highlighted bit, we get 
consecutive 4 bits. 1001111.

An efficient solution is to walk through the bits in binary representation of given number. We keep track of current 1’s sequence length and the previous 1’s sequence length. When we see a zero, update previous Length:

If the next bit is a 1, previous Length should be set to current Length.
If the next bit is a 0, then we can’t merge these sequences together. So, set previous Length to 0.
We update max length by comparing following two:

Current value of max-length
Current-Length + Previous-Length .
result = return max-length+1 (// add 1 for flip bit count )


'''


def findLongestSequenOf1InBinaryRepresentationWithOneFlip(n):
    previous_count = 0
    current_count = 0
    maximum_sequency = float("-inf")

    while n :
        
        # If Current bit is a 1  then increment current_count++ 
        if n & 1 == 1:
            current_count = current_count + 1

        # If Current bit is a 0  
        # then check next bit of a 
        else:
            
            # Update prevLen to 0 (if next bit is 0)  
            if n & 2 == 0:
                previous_count = 0
            #  Update prevLen to current_count if next bit 1   
            else:
                previous_count = current_count    

            # If two consecutively bits  
            # are 0 then currLen also  
            # will be 0
            current_count = 0 
                
        maximum_sequency = max(current_count + previous_count , maximum_sequency)  
        
        # Remove last bit (Right shift) 
        n = n >> 1

    print("maximum_sequency : " , maximum_sequency + 1)    

        
if __name__ == '__main__':
    findLongestSequenOf1InBinaryRepresentationWithOneFlip(1775)
    findLongestSequenOf1InBinaryRepresentationWithOneFlip(12)
