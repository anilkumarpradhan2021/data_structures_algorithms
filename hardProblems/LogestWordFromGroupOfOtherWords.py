'''
Created on 29-Oct-2019

@author: anpradha

Longest Word: Given a list of words, write a program to find the longest word made of other words
in the list.'

EXAMPLE
Input: test, tester, testertest, testing, testingtester
Output: testingtester


'''

''' This works great if the string is combination of 2 other string but it will failed if longest string is combination of more than 2 words'''


def findTheLogestWord(words):
    d = {}
    # Just adding the words to dict
    [d.setdefault(word, word) for word in words]
    
    logestMatch = ""
    for word in words:
        for i in range(len(word)):
            firstHalf = word[:i]
            secondHalf = word[i:]
            #print("firstHalf : " , firstHalf , "secondHalf : " , secondHalf)

            if firstHalf in d and secondHalf in d:
                if len(logestMatch) < len(word):
                    logestMatch = word
    
    print(logestMatch)        


def findTheLogestWordImproved(words):
    d = {}
    
    ''' Just adding the words to dict so that lookup will be O(1)'''
    [d.setdefault(word, word) for word in words]
    
    ''' Just sort the words in decreasing order'''
    sorted(words, key=lambda word : len(word) , reverse=True)

    logestMatch = ""
    
    for word in words:
        if canBuildWord(word, d, True):
            if len(logestMatch) < len(word):
                logestMatch = word
    
    print(logestMatch)        


def canBuildWord(word, map, isOriginal):
        
        ''' base case is word is present in map but its not the original string i.r its a substring of original'''
        if word in map and not isOriginal:
            return True
        
        for i in range(len(word)):
            firstHalf = word[:i]
            secondHalf = word[i:]
            if firstHalf in map and canBuildWord(secondHalf, map, False):
                return True
    
            
if __name__ == '__main__':
    words = ["test", "tester", "testertest", "testing", "testingtester"]
    words = ["test", "tester", "testertest", "testing", "testingtester" , "testtestertestertest"]

    findTheLogestWord(words)
    findTheLogestWordImproved(words)
