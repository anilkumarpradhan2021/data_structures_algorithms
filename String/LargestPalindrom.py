'''
Created on 01-Sep-2016

@author: anpradha

Complexity : O(N2) , space Complexity : O(1)

'''



def findLongestPalindrome(string):
    return max([getPalindromeAt(i, string) for i in range(len(string))], key=lambda a: len(a)) if len(string) > 0 else ''

def getPalindromeAt(position, string):
    longest = (position, position)
    for lower, upper in [(position - 1, position + 1), (position, position + 1)]:
        while lower >= 0 and upper < len(string) and string[lower] == string[upper]:
            upper += 1
            lower -= 1
        longest = max(longest, (lower + 1, upper - 1), key=lambda a: a[1] - a[0])
    return string[longest[0] : longest[1] + 1]

def logestParlindromeMyVersion(string, left, right):
    
    while left >= 0 and  right < len(string) and string[left] == string[right] :
        left = left - 1
        right = right + 1
    return string[left + 1:right]

def findLogestpalindrome(string):
    
    logest_pal = ""
    
    # Find palindrome for all char/position in string 
    for i in range(len(string)):
        '''odd cases like 121 ,  left=position and right=position'''
        temp = logestParlindromeMyVersion(string, i, i)
        
        if len(temp) > len(logest_pal):
            logest_pal = temp
        
        '''even cases like 1221 ,left=position and right=position + 1'''
        temp = logestParlindromeMyVersion(string, i, i + 1)
        
        if len(temp) > len(logest_pal):
            logest_pal = temp
    
    print(logest_pal)    
        


def findLogestpalindrome_all(string):
    
    logest_pal = ""
    
    # Find palindrome for all char/position in string 
    for i in range(len(string)):
        '''odd cases like 121 ,  left=position and right=position'''
        temp1 = logestParlindromeMyVersion(string, i, i)
        temp2 = logestParlindromeMyVersion(string, i, i + 1)
        if len(temp1) > len(temp2) :
            print(temp1)
        else:
            print(temp2)        
        
    
if __name__ == '__main__':
    pass
    # findLogestpalindrome("12145445499")
    findLogestpalindrome_all("aabcb")


