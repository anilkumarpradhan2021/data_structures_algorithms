'''
Created on 25-Sep-2019

@author: anpradha

Count number of bits to be flipped to convert A to B
Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.
Example :

Input : a = 10, b = 20
Output : 4
Binary representation of a is 00001010
Binary representation of b is 00010100
We need to flip highlighted four bits in a
to make it b.

Input : a = 7, b = 10
Output : 3
Binary representation of a is 00000111
Binary representation of b is 00001010
We need to flip highlighted three bits in a
to make it b.



'''


def countNumberOfBitTFlipToMakeAToB(a, b):
    a_xor_b = a ^ b
    
    # count number of set bit
    count = 0
    while a_xor_b:
        if a_xor_b & 1 == 1:
            count = count + 1   
            # shift it to right for next bit
        a_xor_b = a_xor_b >> 1

    print(count)

if __name__ == '__main__':
    countNumberOfBitTFlipToMakeAToB(7, 10)
