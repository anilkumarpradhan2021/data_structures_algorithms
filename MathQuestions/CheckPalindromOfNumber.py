'''
Created on 04-Jul-2017

@author: anpradha
'''

def checkcPalindromOfNumber(number):
    reverse = 0;
    print("Original Number : " + str(number))
    n = number
    while number > 0:
        reverse = reverse * 10 + number % 10
        number = (number // 10)
    print("Reversed Number is : " + str(reverse))
    return reverse == n;
    
        
if __name__ == '__main__':
    print(checkcPalindromOfNumber(121))
