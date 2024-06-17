'''
Created on 28-Oct-2019

@author: anpradha

Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. 
See following examples for more details.
This is a famous Google interview question, also being asked by many other companies now a days.

Consider the following dictionary 
{ i, like, sam, sung, samsung, mobile, ice, 
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes 
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" 
or "i like sam sung".



'''

refernce_dict = {"mobile", "samsung", "sam", "sung",
                            "man", "mango", "icecream", "and",
                            "go", "i", "like", "ice", "cream"}


def wordBreakProblemRecurssion(input, words=[]):
    if len(input) == 0:
        return True
    
    for i in range(1, len(input) + 1):
        
        # add it to word
        words.append(input[:i])
        
        '''
            // Now we will first divide the word into two parts , 
            // the prefix will have a length of i and check if it is  
            // present in dictionary ,if yes then we will check for  
            // suffix of length size-i recursively. if both prefix and  
            // suffix are present the word is found in dictionary. 
        '''
        if input[:i] in refernce_dict and wordBreakProblemRecurssion(input[i:], words):
            return True
        
        # remove it from words as both condition not satisfied
        words.pop()
    return False


def wordBreakProblemWithoutRecurssionWithDP(input):
    
    '''Initialize all values as false.  '''
    aux = [False for i in range(len(input) + 1)]
    
    if len(input) == 0:
        return True
    
    for i in range(1, len(input) + 1):
        
        ''' 
         // if aux[i] is false, then check if current prefix can make it true. 
        // Current prefix is input[:i] 
        '''        
        if aux[i] is False:
            if input[:i] in refernce_dict:
                aux[i] = True
        
        '''
            if input[:i] is a valid word , then check the rest of the word i.r input[i+1:]
        '''
        if aux[i]:
            # If we reached the last prefix 
            if (i == len(input)): 
                return True
            
            for j in range(i + 1, len(input) + 1):
                
                if aux[j] == False and input[i:j] in refernce_dict:
                    aux[j] = True
                
                '''If we reached the last character '''
                if j == len(input) and aux[j] == True:
                    return True    
    
    print(aux)
    return False

    
if __name__ == '__main__':
    word = []
    print(wordBreakProblemRecurssion("ilikesamsung", word))
    print(word)

    print(wordBreakProblemWithoutRecurssionWithDP("ilikesamsung"))
