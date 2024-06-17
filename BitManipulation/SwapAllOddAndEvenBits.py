'''
Created on 26-Sep-2019

@author: anpradha

Swap all odd and even bits
Given an unsigned integer, swap all odd bits with even bits. 

For example, if the given number is 23 (00010111), 
it should be converted to           43 (00101011). 

Every even position bit is swapped with adjacent bit on right side (even position bits are highlighted in binary representation of 23), 
and every odd position bit is swapped with adjacent on left side.


Let the input number be x
1) Get all even bits of x by doing bitwise and of x with 0xAAAAAAAA. The number 0xAAAAAAAA is a 32 bit number with all even bits set as 1 and all odd bits as 0.
2) Get all odd bits of x by doing bitwise and of x with 0x55555555. The number 0x55555555 is a 32 bit number with all odd bits set as 1 and all even bits as 0.
3) Right shift all even bits.
4) Left shift all odd bits.
5) Combine new even and odd bits and return.

    
'''
def swapBits(x) : 
      
    # Get all even bits of x 
    even_bits = x & 0xAAAAAAAA   # same as x & 1010 1010 1010 1010 1010 1010 1010 1010 for 32 bit 
  
    # Get all odd bits of x 
    odd_bits = x & 0x55555555    # same as x & 0101 0101 0101 0101 0101 0101 0101 0101 
      
    # Right shift even bits 
    even_bits >>= 1
    #even_bits = even_bits >> 1
      
    # Left shift odd bits 
    odd_bits <<= 1 
  
    # Combine even and odd bits 
    return (even_bits | odd_bits)  


if __name__ == '__main__':
    print(swapBits(23))