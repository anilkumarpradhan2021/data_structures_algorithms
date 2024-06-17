'''
Created on 29-Oct-2019

Given an input text and an array of k words, arr[], find all occurrences of all words in the input text

@author: anpradha
Input: text = "ahishers"    
       arr[] = {"he", "she", "hers", "his"}

Output:
   Word his appears from 1 to 3
   Word he appears from 4 to 5
   Word she appears from 3 to 5
   Word hers appears from 4 to 7
   
   
'''


def stringSearch(mainString, stringToSerarch, temp_dict):
    for i in range(len(mainString)):
        if mainString[i:i + len(stringToSerarch)] == stringToSerarch:
            temp_dict[stringToSerarch] = temp_dict.get(stringToSerarch, 0) + 1


class Node():

    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie():

    def __init__(self):
        self.root = Node()
    
    def insertWord(self, word):
        temp = self.root
        for wordChar in word:
            if wordChar not in temp.children:
                temp.children[wordChar] = Node()

            temp = temp.children[wordChar]
        temp.isWord = True    
    
    def searchWord(self, word):
        temp = self.root
        print(temp.children)
        for wordChar in word:
            if wordChar not in temp.children:
                return False
            temp = temp.children[wordChar]
        
        if temp and temp.isWord:
            return True
        else:
            return False    

    def searchByWordIndex(self, mainString, i , temp_dict):
        temp = self.root
        for index in range(i, len(mainString)):
            if mainString[index]  not in temp.children:
                break
            
            temp = temp.children[mainString[index]]
            
            if temp.isWord:
                temp_dict[mainString[i:index + 1]] = temp_dict.get(mainString[i:index + 1], 0) + 1 


'''
This algorithm takes 0( kt) time to create the trie and 0( bk) time to search for all the strings.
Reminder: k is the length of the longest string in T, b is the length of the bigger string, and t is
    the number of smaller strings within T

'''


def searchSubstringsInMainString(mainString, substringArray):  
    
    '''create trie with all substringArray'''
    
    root = Trie()
    for word in substringArray:
        root.insertWord(word)
    
    temp_dict = {} 

    for i in range(len(mainString)):  
        root.searchByWordIndex(mainString, i , temp_dict)  
 
    print(temp_dict)                                      


''' easy solution but complexity is O(KBT) , Reminder: k is the length of the longest string in T, b is the length of the bigger string, and t is
    the number of smaller strings within T.
 '''


def searchSubstringsInMainString2(mainString, substringArray):  
    
    temp_dict = {} 

    for word in substringArray:  
        stringSearch(mainString, word, temp_dict) 
 
    print(temp_dict)                                      


if __name__ == '__main__':
    # mainString = "anil kumar pradhan anil ani"
    # stringToSerarch = "anil"
    # stringSearch(mainString, stringToSerarch)
    
    substringArray = {"is", "ppi", "hi", "sis", "i", "ssippi"}
    mainString = "mississippi"
    searchSubstringsInMainString(mainString, substringArray)
    searchSubstringsInMainString2(mainString, substringArray)
