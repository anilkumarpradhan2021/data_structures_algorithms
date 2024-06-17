'''
Created on 25-Sep-2019

@author: anpradha

Count set bits in an integer
Write an efficient program to count number of 1s in binary representation of an integer.

Examples :

Input : n = 6
Output : 2
Binary representation of 6 is 110 and has 2 set bits

Input : n = 13
Output : 3
Binary representation of 13 is 1101 and has 3 set bits



'''

'''

Complexity O(logn)
'''

def countNumberOfSetBits(num):
    # reference count bit 
    num_to_bits=[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4];  
    
    if num == 0:
        return 0
    if num > 0:
        nible = num & 0xF
        num  = num >> 4
        return num_to_bits[nible] + countNumberOfSetBits(num)
        
    
def countSetBit(n):
    count = 0
    while n > 0 :
        if n & 1 == 1:
            count = count + 1
        
        n = n >> 1
    
    print(count)    


'''
# Recursively get nibble of a given number and map them in the array 


'''
def countSetBit2(n):
    # This represent 0 to 15 with number of bit they contain
    num_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4];  
    
    # As we store the bit number till 15, idea is we will keep on dividing the number with 15 and add number to it 
    
    nible = 0 
    
    if n == 0:
        return num_to_bits[0]

    else:
        # Find last nibble 
        nible = n & 15  # we can use 0xf as well same
        n = n >> 4
        return num_to_bits[nible] + countSetBit2(n)


if __name__ == '__main__':
    countSetBit(6)
    countSetBit(13)

    print(countSetBit2(6))
    print(countSetBit2(13))
    print(countNumberOfSetBits(13))
