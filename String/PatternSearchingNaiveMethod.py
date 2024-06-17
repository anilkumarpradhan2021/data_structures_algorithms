'''
Created on 13-Oct-2019

@author: anpradha

Algorithm for Pattern Searching

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
        
        
'''


def naivePatternSearch(txt, patt):
    for i in range(len(txt) - len(patt) + 1):
        j = 0
        while j < len(patt):
            if txt[i + j] != patt[j]:
                break
            if j == (len(patt) - 1):
                print("Pattern matched at index : " , i)    

            j = j + 1


def naivePatternSearch2(txt, patt):
    for i in range((len(txt) - len(patt) + 1)):
        if txt[i:(i + len(patt))] == patt:
            print("Pattern matched at index : " , i)    

                
if __name__ == '__main__':
    txt = "AABAACAADAABAABA"
    patt = "AABA"
    naivePatternSearch(txt, patt)
    print("8888888888888888")
    naivePatternSearch2(txt, patt)
