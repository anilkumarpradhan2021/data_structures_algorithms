'''
Created on 17-Sep-2019

@author: anpradha

Given two strings str1 and str2, find if str1 is a subsequence of str2. 
A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements 
(source: wiki). Expected time complexity is linear.

Examples :

Input: str1 = "AXY", str2 = "ADXCPY"
Output: True (str1 is a subsequence of str2)

Input: str1 = "AXY", str2 = "YADXCP"
Output: False (str1 is not a subsequence of str2)

Input: str1 = "gksrek", str2 = "geeksforgeeks"
Output: True (str1 is a subsequence of str2)


'''


# Returns true if str1 is a subsequence of str2 
# m is length of str1, n is length of str2 
def isSubSequence(str1, str2, m, n): 
      
    j = 0  # Index of str1 
    i = 0  # Index of str2 
      
    # Traverse both str1 and str2 
    # Compare current character of str2 with  
    # first unmatched character of str1 
    # If matched, then move ahead in str1 
      
    while j < m and i < n: 
        if str1[j] == str2[i]:     
            j = j + 1    
        i = i + 1
          
    # If all characters of str1 matched, then j is equal to m 
    return j == m 


if __name__ == '__main__':
    str1 = "AXY"
    str2 = "ADXCPY"
    
    print(isSubSequence(str1, str2, len(str1), len(str2)))