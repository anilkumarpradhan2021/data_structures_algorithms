'''
Created on 13-Aug-2019

@author: anpradha


video for understanding:
https://www.youtube.com/watch?v=GTJr8OvyEVQ

KMP Algorithm for Pattern Searching
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
Examples:

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
        
     
The time complexity of KMP algorithm is O(n) in the worst case.   
'''


def kmp(text, pat):
    
    lps = [0] * len(pat)
    preProcessPattern(pat, lps)
    print(lps)
    i = 0
    j = 0
    
    while i < len(text):
        
        # if pat and text match increase i and j
        if text[i] == pat[j]:
            i = i + 1
            j = j + 1
        
        # if not match
        else:
            # if j is not 0 then get the j value from lps array            
            if j != 0:
                j = lps[j - 1]
            else:
                i = i + 1    
        
        if j == len(pat):
            print("Substring Present: " , i - j)    
            j = lps[j - 1]
            

def preProcessPattern(pat, lps): 
    j = 0  # jth of the previous longest prefix suffix 
    lps[0] = 0  # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < len(pat): 
        if pat[i] == pat[j]: 
            j = j + 1
            lps[i] = j
            i = i + 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if j != 0: 
                j = lps[j - 1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = j 
                i = i + 1
                

if __name__ == '__main__':
    text = "ABABDABACDABABCABABABABCABAB"
    pat = "ABABCABAB"
    kmp(text, pat)
    
