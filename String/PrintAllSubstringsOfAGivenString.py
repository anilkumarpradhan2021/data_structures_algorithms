'''
Created on 29-Jul-2019

@author: anpradha
'''

'''


Program to print all substrings of a given string
Given a string as an input. We need to write a program that will print all non-empty substrings of that given string.

Examples :

Input :  abcd
Output :  a 
          b
          c
          d
          ab
          bc
          cd
          abc
          bcd
          abcd



'''
if __name__ == '__main__':
    arr = list("abcd")
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i:j + 1])
