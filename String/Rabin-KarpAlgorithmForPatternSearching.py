'''
Created on 13-Oct-2019

@author: anpradha


Python Program for Rabin-Karp Algorithm for Pattern Searching
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
      
      
    Note:
    Just remember the formula 
    M = len(pattern)
    h = math.pow(d, M - 1) % prime_number     
    d = is the number of characters in the input alphabet 
    txt_hash = (d * (txt_hash - ord(txt[i]) * h) + ord(txt[i + M])) % prime_number 

    
    Worst case :  O(mn).  
   
   https://www.youtube.com/watch?v=H4VrKHVG5qI   
   
https://brilliant.org/wiki/rabin-karp-algorithm/


     
'''

import math

# d is the number of characters in the input alphabet 
d = 256
  
# pat  -> pattern 
# txt  -> text 
# prime_number    -> A big prime number 

  
def search(pat, txt, prime_number): 
    M = len(pat) 
    N = len(txt) 
    pat_hash = 0  # hash value for pattern 
    txt_hash = 0  # hash value for txt 
    h = 1
  
    # The value of h would be "pow(d, M-1)%prime_number" 
    h = math.pow(d, M - 1) % prime_number
  
    # Calculate the hash value of pattern and first window 
    # of text 
    for i in range(M): 
        pat_hash = (d * pat_hash + ord(pat[i])) % prime_number 
        txt_hash = (d * txt_hash + ord(txt[i])) % prime_number 
  
    # Slide the pattern over text one by one 
    for i in range(N - M + 1): 
        # Check the hash values of current window of text and 
        # pattern if the hash values match then only check 
        # for characters on by one 
        if pat_hash == txt_hash: 
            # Check for characters one by one 
            for j in range(M): 
                if txt[i + j] != pat[j]: 
                    break
  
            j += 1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1] 
            if j == M: 
                print("Pattern found at index " + str(i))
  
        # Calculate hash value for next window of text: Remove 
        # leading digit, add trailing digit 
        if i < N - M: 
            txt_hash = (d * (txt_hash - ord(txt[i]) * h) + ord(txt[i + M])) % prime_number 
  
            # We might get negative values of t, converting it to 
            # positive 
            if txt_hash < 0: 
                txt_hash = txt_hash + prime_number 


prime = 101


def pattern_matching(text, pattern):
    m = len(pattern)
    n = len(text)
    pattern_hash = create_hash(pattern, m)
    text_hash = create_hash(text, m)

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Check for characters one by one 
            for j in range(m): 
                if txt[i + j] != pat[j]: 
                    break
            j = j + 1 
            if j == m:
                print("Pattern found at index " + str(i))
                       
        if i < n - m :    
            text_hash = recalculate_hash(text, i, i + m, text_hash, m)
    
    
def create_hash(input, end):
    hash = 0
    ''' H(“abc”)= ord("a")^0 + ord("b")^1 + ord("c")^2 '''
    for i in range(end):
        hash = hash + ord(input[i]) * pow(prime, i)
    return hash


def recalculate_hash(input, old_index, new_index, old_hash, pattern_len):
    new_hash = old_hash - ord(input[old_index])
    new_hash = new_hash / prime
    new_hash = new_hash + ord(input[new_index]) * pow(prime, pattern_len - 1)
    return new_hash;


if __name__ == '__main__':
    txt = "AABAACAADAABAABA"
    pat = "AABA"
    # search(pat, txt, 101)
    pattern_matching(txt, pat)
