'''
Created on 30-Oct-2019

@author: anpradha

Find all strings that match specific pattern in a dictionary
Given a dictionary of words, find all strings that matches the given pattern where every character in the pattern is uniquely mapped to a character in the dictionary.

Examples:

Input:  
dict = ["abb", "abc", "xyz", "xyy"];
pattern = "foo"
Output: [xyy abb]
Explanation: 
xyy and abb have same character at index 1 and 2 like the pattern

Input:  
dict = ["abb", "abc", "xyz", "xyy"];
pat = "mno"
Output: [abc xyz]
Explanation: 
abc and xyz have all distinct characters, similar to the pattern

Input:  
dict = ["abb", "abc", "xyz", "xyy"];
pattern = "aba"
Output: [] 
Explanation: 
Pattern has same character at index 0 and 2. 
No word in dictionary follows the pattern.

Input:  
dict = ["abab", "aba", "xyz", "xyx"];
pattern = "aba"
Output: [aba xyx]
Explanation: 
aba and xyx have same character at index 0 and 2 like the pattern


IDEA:
The idea is to encode the pattern in such a way that any word from the dictionary that matches the pattern will have same hash as that of the pattern after encoding. We iterate through all words in dictionary one by one and print the words that have same hash as that of the pattern.
step
1. create a encoded value for pattern
2. create a encoded value for each word in dict
3. if both match , print 
4. else dont print


'''


def encodeString(word):
    d = {}
    encodedHash = ""
    for i in range(len(word)):
        if word[i] not in d:
            d[word[i]] = i
        
        encodedHash = encodedHash + str(d[word[i]])
    
    print(encodedHash)
    return encodedHash    


def findMatchedWords(words , pattern):
    for word in words:
        if len(word) == len(pattern) and encodeString(word) == encodeString(pattern):
            print(word)


if __name__ == '__main__':

    words = ["abb", "abc", "xyz", "xyy"]
    pattern = "aba"

    words = ["abb", "abc", "xyz", "xyy"]
    pattern = "foo"
    

    findMatchedWords(words , pattern)
