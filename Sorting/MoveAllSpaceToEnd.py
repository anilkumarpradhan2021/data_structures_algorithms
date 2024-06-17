'''
Created on 13-Sep-2016

@author: anpradha

Problem:
Given a String that has set of words and spaces , Program to move all the spaces to front of string 
e.g
s = "Anil kumar Pradhan"
o/p = "   AnilKumarPradhan" 

Time Complexity  O(n)


Problem :
1. Move all space to end
2. Move all space to beginning
3. Move all 0 to end 

'''   

def moveSpaceToFront(str):
    ''' Converting string into list'''
    temp = list(str)
    print(temp)
    count = len(temp) - 1
    string_length = len(temp)
    
    ''' for loop from last index to 0 Syntax for range(start_index,end_index,decrement)  end_index is excluded so -1 else 0'''
    for i in range(string_length - 1, -1, -1):
        if not temp[i].isspace():
            temp[count] = temp[i]
            count = count - 1
    
    while count >= 0:
        temp[count] = " "
        count = count - 1
        
    print(temp)  
    return "".join(temp)


def moveSpaceToEnd(str):
    ''' Converting string into list'''
    temp = list(str)
    print(temp)
    count = 0
    
    ''' for loop from last index to 0 Syntax for range(start_index,end_index,decrement)  end_index is excluded so -1 else 0'''
    for i in range(0, len(str)):
        if not temp[i].isspace():
            temp[count] = temp[i]
            count = count + 1
    
    while count < len(str):
        temp[count] = " "
        count = count + 1
        
    print(temp)  
    return "".join(temp)
    

def moveZeroToEnd(arr):
    count = 0
    
    ''' for loop from last index to 0 Syntax for range(start_index,end_index,decrement)  end_index is excluded so -1 else 0'''
    for i in range(0, len(arr)):
        if arr[i] > 0:
            arr[count] = arr[i]
            count = count + 1
    
    while count < len(arr):
        arr[count] = 0
        count = count + 1
        
    return arr


if __name__ == '__main__':
    print("Move all Space to Beginning")
    str = "Anil Kumar Pradhan"
    str = moveSpaceToFront(str)
    print(str)
    
    print("Move all Space to End")
    str = "Anil Kumar Pradhan"
    str = moveSpaceToEnd(str)
    print(str)
    
    print("Move all Zero to end")
    
    arr = [1, 0, 3, 2, 0, 4, 5, 50, 0]
    arr = moveZeroToEnd(arr)
    print(arr)
