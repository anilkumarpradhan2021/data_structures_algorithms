'''
Created on 22-Aug-2019

@author: anpradha

Find the longest substring with k unique characters in a given string
Given a string you need to print longest possible substring that has exactly M unique characters. If there are more than one substring of longest possible length, then print any one of them.
Examples:

"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message. 

'''


def logestSubstringWithKUniqueChar(arr, k):
    i = 0
    j = 0
    max_length = float("-inf")
    d = {}
    
    while i < len(arr):
        if arr[i] in d:
            d[arr[i]] = d[arr[i]] + 1 
        else:
            d[arr[i]] = 1 
        i = i + 1
        
        while len(d) > k:
            d[arr[j]] = d[arr[j]] - 1
            if d[arr[j]] == 0:
                d.pop(arr[j]) #  or can use del d[arr[j]]
            j = j + 1    
        max_length = max(max_length, sum(d.values()))    
    
    print(max_length)    

        
if __name__ == '__main__':
    logestSubstringWithKUniqueChar("aabbcc", 2)
