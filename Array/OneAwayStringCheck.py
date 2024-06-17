'''
Created on 20-Sep-2019

@author: anpradha
Check if edit distance between two strings is one
An edit between two strings is one of the following changes.

Add a character
Delete a character
Change a character
Given two string s1 and s2, find if s1 can be converted to s2 with exactly one edit. Expected time complexity is O(m+n) where m and n are lengths of two strings.

Examples:



Input:  s1 = "geeks", s2 = "geek"
Output: yes
Number of edits is 1

Input:  s1 = "geeks", s2 = "geeks"
Output: no
Number of edits is 0

Input:  s1 = "geaks", s2 = "geeks"
Output: yes
Number of edits is 1

Input:  s1 = "peaks", s2 = "geeks"
Output: no
Number of edits is 2


https://www.geeksforgeeks.org/check-if-two-given-strings-are-at-edit-distance-one/

Time complexity: O(n)
Auxiliary Space: O(1)


'''


def oneAway(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    ''' if the length difference is more than 1 , exit'''
    if abs(len_str1 - len_str2) > 1:
        print("Not One away distance")
    
    str1_index = 0 
    str2_index = 0 
    
    count = 0
    
    while str1_index < len_str1 and str2_index < len_str2:
        if str1[str1_index] != str2[str2_index]:
            
            if count == 1:
                print("char diff is more than One")
                return False
            
            ''' if string1 > string2'''
            if len_str1 > len_str2:
                str1_index = str1_index + 1

            elif len_str2 > len_str1:
                str2_index = str2_index + 1
            
            # both have same length
            else:
                str1_index = str1_index + 1
                str2_index = str2_index + 1
            count = count + 1                             
        else:
            str1_index = str1_index + 1
            str2_index = str2_index + 1     
    
    '''    # if last character is extra in any string  '''
    if  str1_index < len_str1 or str2_index < len_str2:
        count = count + 1 

    if count > 1:
        print("char diff is more than One")
        return False

    return True


if __name__ == "__main__":
    str1 = "pale"
    str2 = "pake"
    print(oneAway(str1, str2))
    
