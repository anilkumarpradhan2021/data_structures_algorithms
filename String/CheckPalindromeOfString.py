'''
Created on 03-Dec-2017

@author: anpradha



Algorithm:
isPalindrome(str)
1) Find length of str. Let length be n.
2) Initialize low and high indexes as 0 and n-1 respectively.
3) Do following while low index ‘l’ is smaller than high index ‘h’.
…..a) If str[l] is not same as str[h], then return false.
…..b) Increment l and decrement h, i.e., do l++ and h–.
4) If we reach here, it means we didn’t find a mis


'''

def checkPalindrome(str):
    
    # lower index 
    lower_index = 0
    
    #higher index
    higher_index = len(str) -1
    while higher_index > lower_index:
        if str[higher_index] !=str[lower_index]:
            return False
        
        higher_index = higher_index -1
        lower_index = lower_index + 1
    return True     
    
    
if __name__ == '__main__':
    print(checkPalindrome("AAAA"))