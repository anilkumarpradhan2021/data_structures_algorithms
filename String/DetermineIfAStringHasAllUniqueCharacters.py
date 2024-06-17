'''
Created on 21-Nov-2019

@author: anpradha

Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?


'''


def isAllUnique(string) -> bool:
    flag = 0
    
    for i in range(len(string)):
        
        bitNumber = abs(ord("a") - ord(string[i]))
        
        ''' find the bitNumber from flag '''
        if (1 << bitNumber) & flag > 0:
            print("Not having unique chars : " , string)
            return False
        else:
            flag = flag | (1 << bitNumber)
    print("Having unique chars : " , string)            
    return True        
            
            
            

if __name__ == '__main__':
    print(isAllUnique("GeeksforGeeks"))
    print(isAllUnique("abc"))
