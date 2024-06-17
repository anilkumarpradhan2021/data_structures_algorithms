'''
Created on 05-Nov-2019

@author: anpradha
Manachar’s Algorithm


Manacher's Algorithm has one single application. It is used to find the Longest Palindromic Sub-string in any string. 
This algorithm is required to solve sub-problems of some very hard problems.

Bit difficult to understand :)

https://www.youtube.com/watch?v=nbTSfrEfo6M



'''


def convertToNewString(string):
    newString = "%"
    
    for i in string:
        newString = newString + "$" + i 
    
    newString = newString + "$" + "&"    
    
    print(newString)
    return newString


def longestPalindromeSubstring(string):
    newString = convertToNewString(string)
    currentPivot = 0
    rightLimit = 0
    
    p = [0 for i in range(len(newString))]
    
    for i in range(1, len(newString) - 1):
        iMirror = 2 * currentPivot - i
        
        if i < rightLimit:
            p[i] = min(rightLimit - i , p[iMirror])
            
        while newString[i + 1 + p[i]] == newString[i - 1 - p[i]]:
            p[i] = p[i] + 1
        
        if i + p[i] > rightLimit:
            currentPivot = i
            rightLimit = i + p[i]   
    
    print("p : " , p)
    
    '''
        // Find the longest palindrome length in p.

    '''
    maxPalindrome = 0
    centerIndex = 0
    
    for i in range(len(p)):
        if p[i] > maxPalindrome:
            maxPalindrome = p[i];
            centerIndex = i;
    
    startIndex = (centerIndex - 1 - maxPalindrome) // 2
    endIndex = maxPalindrome
    print("Maximum palindrome : " , string[startIndex:endIndex + 1])    

                        
if __name__ == '__main__':
    string = "abababa"
    string = "caba"
    longestPalindromeSubstring(string)
