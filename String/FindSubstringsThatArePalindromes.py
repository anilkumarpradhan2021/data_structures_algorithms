'''
Created on 03-Nov-2019

@author: anpradha
Find all distinct palindromic sub-strings of a given string
Given a string of lowercase ASCII characters, find all distinct continuous palindromic sub-strings of it.
Examples:

Input: str = "abaaa"
Output:  Below are 5 palindrome sub-strings
a
aa
aaa
aba
b


Input: str = "geek"
Output:  Below are 4 palindrome sub-strings
e
ee
g
k

'''


'''
O(n3)

'''


def bruteForceMethod(str):
    s = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            t = str[i:j + 1]
            if t == t[::-1]:
                s.add(t)
                 
    print("palindrome : " , s)


''' 
Considering each character as a pivot, expand on both sides to find the length of both even and odd length palindromes centered at the pivot character under consideration .
Time complexity for this step is O(n^2)

https://www.techiedelight.com/find-possible-palindromic-substrings-string/


O(n2)

'''


def expand(string, low, high, allPossibleEvenAndOddPalindrom):
    while low >= 0 and high < len(string) and string[low] == string[high]:
        allPossibleEvenAndOddPalindrom.add(string[low:high + 1])
        low = low - 1
        high = high + 1

            
def palindromicSubStrings(string):
    allPossibleEvenAndOddPalindrom = set()
    for i in range(len(string)):  
        
        ''' for all odd numbered palindrum like a , aaa , aaaaa'''
        expand(string, i, i, allPossibleEvenAndOddPalindrom)
        
        ''' for all even numbered palindrum like aa, aaaa '''
        expand(string, i, i + 1, allPossibleEvenAndOddPalindrom)
    
    print("allPossibleEvenAndOddPalindrom : " , allPossibleEvenAndOddPalindrom)

     
if __name__ == '__main__':
    bruteForceMethod("abaaa")
    palindromicSubStrings("abaaa")
