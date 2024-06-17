'''
Created on 27-Sep-2019

@author: anpradha
'''


def solution1():
    str = "Location 'Welcome  to india' Bangalore Channai 'IT city'  Mysores"
    print(str)
    str = str.rstrip().lstrip()
    print(str)
    flag = True
    result = []
    temp = ""
    for i in str:
        
        if i == "'":
            flag = not flag
        
        if i == " " and flag:
            result.append(temp)
            temp = ""
        else:
            temp = temp + i 
    result.append(temp)  
    result = [i for i in result if i != ""]
    print("---------------")      
    for i in result:
        print(i)


def solution2():
    str = "Location 'Welcome  to india' Bangalore Channai 'IT city'  Mysores"
    token = False
    currentWord = ""
    for i in range(len(str)):
        if str[i] == "'": 
            token = not token   
        currentWord = currentWord + str[i]
        if (str[i] == " " and token == False) or (i == len(str) - 1):
            print(currentWord)
            currentWord = ""
    #print(currentWord)        
                

if __name__ == '__main__':
    solution2()
