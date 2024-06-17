'''
Created on 08-Aug-2019

@author: anpradha



Naive algorithm for Pattern Searching
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. 
You may assume that n > m.

Examples:

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

Complexity :  worst case is O(m*(n-m+1)) , best O(n)

'''


def patternMatch(txt, pat):
    txt_size = len(txt)
    pat_size = len(pat)
    
    for i in range(0, txt_size - pat_size + 1):
        for j in range(0, pat_size):
            if txt[j + i] != pat[j]:
                break
            
            if j == pat_size - 1 :
                print("Pattern Matched at index : " , i)
                
    
if __name__ == '__main__':
    txt = "THIS IS A TEST TEXT TEST"
    pat = "TEST"
    # patternMatch(txt, pat)
    txt = "AABAACAADAABAAABAAAABA"
    pat = "AABA"
    patternMatch(txt, pat)
    
