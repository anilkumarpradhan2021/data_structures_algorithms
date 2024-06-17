'''
Created on 12-Oct-2016

@author: anpradha

Problem :
Input: A Number

Out­put: Dec­i­mal of reversed binary rep­re­sen­ta­tion of a number.


Exam­ple:

Input : 30
Output : 15

Explanation:

binary representation of 30 is : 11110
reverse of binary representation : 01111
decimal of reversed binary representation is : 15


Approach:


1. Ini­tial­ize int res =0
2 .Now from a num­ber , take one bit at a time
3. take AND of that bit with 1 and 
        then OR with res and store it in res
4. make right shift in num­ber by 1
5. make left shift in res by 1

'''


def checkIfKthBitIsOnOrOff(n, k):
    if n & (1 << (k - 1)):
        return 1
    else:
        return 0


''' Let consider its 32 bit so from left to right just print the bit'''
def decimal_to_binary(number):
    print("Number is : " + str(number))
    
    ''' Lets its 32 bit number'''
    
    for i in range(31, 0, -1):
        print(checkIfKthBitIsOnOrOff(number, i), end=' ')
    print()    

        
    
if __name__ == '__main__':
    number = 30
    res = 0
    decimal_to_binary(number)
    ''' find the number of bit in the number '''
    s = number.bit_length()
    while number :
        ''' left shift nReserve'''
        res = res << 1  
        res = res | (number & 1)
        ''' right shift number'''
        number = number >> 1
    
    print(res) 
    decimal_to_binary(res)
