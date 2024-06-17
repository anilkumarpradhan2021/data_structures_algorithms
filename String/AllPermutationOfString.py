'''
Created on 02-Sep-2016

@author: anpradha

time complexity n * n!
'''

'''
Level -1
Permute(ABC, 0, 2)
    i = 0
    Swap (A,A)
    Permute(ABC,1,2)
    Swap(A,A)
    
    i =1
    Swap (A,B)
    Permute(BAC,1,2)
    Swap(B,A)
    
  
    i = 2
    Swap (A,C)
    Permute(CBA,1,2)
    Swap(C,A)
    

'''


def permute(string, start_index, end):
    if start_index == end :
        print(string)
    else:
        for i in range(start_index, end + 1):
            ''' swap '''
            string[start_index], string[i] = string[i], string[start_index]
            permute(string, start_index + 1, end)
            ''' swap '''
            string[start_index], string[i] = string[i], string[start_index]  # back tracking like if AB is done then BA


def permute_string2(str1):
    
    if len(str1) == 0:
        return []
    
    if len(str1) == 1:
        return [str1]
    
    permutation_list = []
    
    for index in range(len(str1)):
        
        start_char = str1[index]
        
        left_over_char = str1[:index] + str1[index + 1:]
        
        for per in permute_string2(left_over_char):
            permutation_list.append([start_char] + per)

    return permutation_list    


def permutation(lst): 
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = []  # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
        m = lst[i] 
  
        # Extract lst[i] or m from the list.  remLst is 
        # remaining list 
        remLst = lst[:i] + lst[i + 1:] 
  
        # Generating all permutations where m is first 
        # element 
        for p in permutation(remLst): 
            l.append([m] + p) 
    return l 


            
        
if __name__ == '__main__':
    pass
    str_list = list("abc")
    #permute(str_list, 0, len(str_list) - 1)
    print(permute_string2(str_list))
