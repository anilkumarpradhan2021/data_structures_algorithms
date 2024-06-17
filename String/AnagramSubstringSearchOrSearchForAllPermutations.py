'''
Created on 13-Oct-2019

@author: anpradha


Anagram Substring Search (Or Search for all permutations)

Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] and its permutations (or anagrams) in txt[]. You may assume that n > m.
Expected time complexity is O(n)

Examples:

1) Input:  txt[] = "BACDGABCDA"  pat[] = "ABCD"
   Output:   Found at Index 0
             Found at Index 5
             Found at Index 6
2) Input: txt[] =  "AAABABAA" pat[] = "AABA"
   Output:   Found at Index 0
             Found at Index 1
             Found at Index 4
             
             
    anagram means : 2 words said to be anagram if they contain same set of char , order doesnot matter   
    e.g
    cat < - > tac
 
 for reference :
 https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/
          
'''


def anaramSearch(txt, pat):
    # create dict for patt 
    patt_dict = {}
    for i in pat:
        patt_dict[i] = patt_dict.get(i, 0) + 1

    # create dict for txt (window size as pat) 
    txt_dict = {}
    for i in txt[:len(pat)]:
        txt_dict[i] = txt_dict.get(i, 0) + 1
    
    print("patt_dict : " , patt_dict)
    print("txt_dict : " , txt_dict)
    
    for i in range(len(pat), len(txt)):
        
        if patt_dict == txt_dict:
            print("pattern match found at index :" , i - len(pat))
            
        # update the dict with new char and remove the oldest char
        txt_dict[txt[i]] = txt_dict.get(txt[i], 0) + 1
        
        # remove the oldest char
        if txt_dict[txt[i - len(pat)]] > 1:
            txt_dict[txt[i - len(pat)]] = txt_dict[txt[i - len(pat)]] - 1
        else:
            del txt_dict[txt[i - len(pat)]]    
    
    ''' this is for scenario when there is a pattern match at the end of the txt'''
    if patt_dict == txt_dict:
        print("pattern match found at index :" , len(txt) - len(pat))
         
            
if __name__ == '__main__':
    txt = "BACDGABCDA"
    pat = "ABCD"
    anaramSearch(txt, pat)
