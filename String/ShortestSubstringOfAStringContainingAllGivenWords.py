'''
Created on 08-Nov-2019

@author: anpradha


Shortest substring of a string containing all given words

Print the shortest sub-string of a string containing all the given words.

In the first example, two solutions are possible: “world is here. this is a life full of ups” and “ups and downs. life is world”.
        sentence = "The world is here. this is a life full of ups and downs. life is world."
        words = { "life", "ups", "is", "world" }; 
        o/p = ups and downs. life is 


https://www.geeksforgeeks.org/shortest-substring-string-containing-given-words/


'''

if __name__ == '__main__':
    sentence = "The world is here. this is a life full of ups and downs. life is world"
    words = ["life", "ups", "is", "world"]
    
    ''' create a hash so that look up will be fast'''
    d = {}
    [d.setdefault(word, 0) for word in words]
    print(d)
    
    wordsInSetence = sentence.split(" ")
    print(wordsInSetence)
    
    numberOfwordFound = 0
    for index in range(len(wordsInSetence)):
        if wordsInSetence[index] in d:
            
            ''' if first time we find this word , then add increase numberOfwordFound'''
            if d[wordsInSetence[index]] == 0:
                numberOfwordFound = numberOfwordFound + 1
            d[wordsInSetence[index]] = index
        
        ''' found all words atleast once '''        
        if  numberOfwordFound == len(d):
            
            ''' find the smallest index of any word in the sequence'''
            min_index = min(d.values())
            max_index = max(d.values())
            print(wordsInSetence[min_index:max_index + 1])
        
