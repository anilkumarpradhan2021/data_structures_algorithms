'''
Created on 06-May-2017

@author: anpradha
'''

def is_palindrome(str):
    start_index = 0
    end_index = len(str) - 1 
    while end_index > start_index:
        if str[start_index] != str[end_index]:
            return False
        start_index = start_index + 1
        end_index = end_index - 1
    return True

if __name__ == '__main__':
    str = input("Please enter a string to check for Palindrome : \n") 
    print(is_palindrome(str))
