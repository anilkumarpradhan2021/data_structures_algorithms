'''
Created on 24-Sep-2019

@author: anpradha

Converting a Real Number (between 0 and 1) to Binary String
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print” ERROR:’
Examples:

Input :  (0.625)10
Output : (0.101)2

Input : (0.72)10
Output : ERROR


'''


def convertToBinaryString(num):
    # check if the number is a real number or not
    # Check if the number is Between 0 to 1 or Not 
    
    print("Number  : ", num)
    result = "."
    if num > 1 or num < 0:
        print("ERROR")
    
    while num > 0:

        # Setting a limit on length: 32 characters 
        if(len(result) >= 32): 
            print("Length of result is more than 32 char")
            print(result)
            break

        b = 2 * num
        
        if b >= 1:
            result = result + "1"
            num = b - 1
        else:
            result = result + "0"
            num = b  
    
    print("Binary is : ", result)    

    
if __name__ == '__main__':
    num = 0.625
    convertToBinaryString(num)
    num = 0.72
    convertToBinaryString(num)
    
