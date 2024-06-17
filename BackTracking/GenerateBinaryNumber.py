'''
Created on 19-Sep-2016

@author: anpradha
'''
'''
An Interesting Method to Generate Binary Numbers from 1 to n
Given a number n, write a function that generates and prints all binary numbers with decimal values from 1 to n.

Examples:

Input: n = 2
Output: 1, 10

Input: n = 5
Output: 1, 10, 11, 100, 101

'''

def decimal_to_binary(number):
    s = []
    while number > 0 :
        s = [number % 2] + s 
        number = number // 2
    print(" Binary  " + str(s))            

if __name__ == '__main__':
    k = 5
    for i in range(1, k + 1):
        print("Number : " + str(i) , end=" ")
        decimal_to_binary(i)
        
