'''
Created on 02-Oct-2019

@author: anpradha



Given a sequence of words, print all anagrams together | Set 1

Given an array of words, print all anagrams together. For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”}, then output may be “cat tac act dog god”.

anagram means:
2 String should have same char in each , position can differ
eg. cat and tac

ANS:
1. create a hash
2. read a word and sort it and add to hashtable
3. repeat for all 
4. print all the values in hashtable group by key 
'''


def printAnagramToether(arr):
    d = {}
    for word in arr:
        hashkey = "".join(sorted(word))
        if hashkey in d:
            d[hashkey].append(word) 
        else:
            d[hashkey] = [word]
    print(d)


if __name__ == '__main__':
    arr = ["cat", "dog", "tac", "god", "act"]
    printAnagramToether(arr)
