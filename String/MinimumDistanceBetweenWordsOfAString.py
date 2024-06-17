'''
Created on 11-Oct-2019

@author: anpradha

Minimum Distance Between Words of a String

Given a string s and two words w1 and w2 that are present in S. The task is to find the minimum distance between w1 and w2. Here distance is the number of steps or words between the first and the second word.

Examples:

    Input : s = “geeks for geeks contribute practice”, w1 = “geeks”, w2 = “practice”
    Output : 1
    There is only one word between closest occurrences of w1 and w2.
    
    
'''


def minimumDistanceBetweenWords(s, word1, word2):
    print(s)
    loc_word1 = -1
    loc_word2 = -1
    min_distance = float("+inf")
    
    for index in range(len(s)):
        if s[index] == word1:
            loc_word1 = index
        if s[index] == word2:
            loc_word2 = index
    
        if loc_word1 != -1 and loc_word2 != -1:
            min_distance = min(min_distance, abs(loc_word1 - loc_word2))
    print("location of word : {word1}  : ".format(word1=word1) , loc_word1)
    print("location of word : {word2}  : ".format(word2=word2), loc_word2)    
    print("min_distance ", min_distance - 1)    


if __name__ == '__main__':
    s = "the quick the brown quick brown the frog"
    word1 = "quick"
    word2 = "frog"
    s = s.split(" ")
    minimumDistanceBetweenWords(s, word1, word2)


    s = "geeks for geeks contribute practice"
    word1 = "geeks"
    word2 = "practice"
    s = s.split(" ")
    minimumDistanceBetweenWords(s, word1, word2)
