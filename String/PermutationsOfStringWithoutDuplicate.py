'''
Created on 05-Oct-2019

@author: anpradha

Permutations with Duplicates: 
Write a method to compute all permutations of a string whose
characters are not necessarily unique. The list of permutations should not have duplicates.
Input : AAB
Output : AAB ABA BAA


check Book : cracking the coding interview 369 page

'''


def calculateFrquencyOfChar(dict, str1):
    for i in str1:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    return dict


def printPerms(dict, prefix, remaining, result):

    'Base case. Permutation has been completed.'    
    if remaining == 0:
        result.append(prefix)
        return 
    
    for c in dict.keys():
        char_count = dict[c]
        if char_count > 0:
            dict[c] = dict[c] - 1
            printPerms(dict, prefix + c, remaining - 1 , result)
            dict[c] = char_count
            
                
def printPermutaion(str1):
    result = []
    dict = {}
    calculateFrquencyOfChar(dict, str1)
    print(dict)
    
    printPerms(dict=dict, prefix="", remaining=len(str1), result=result)
    print(result)

    
if __name__ == '__main__':
    str1 = "AAB"
    str1 = "ABCA"
    printPermutaion(str1)
   
