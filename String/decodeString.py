'''
Created on 17-Sep-2019

@author: anpradha

Decode a string recursively encoded as count followed by substring
An encoded string (s) is given, the task is to decode it. The pattern in which the strings are encoded is as follows.

<count>[sub_str] ==> The substring 'sub_str' 
                      appears count times.
Examples:

Input : str[] = "1[b]"
Output : b

Input : str[] = "2[ab]"
Output : abab

Input : str[] = "2[a2[b]]"
Output : abbabb

Input : str[] = "3[b2[ca]]"
Output : bcacabcacabcaca

The idea is to use two stacks, one for integers and another for characters.
Now, traverse the string,

1 . Whenever we encounter any number, push it into the integer stack 
2. in case of any alphabet (a to z) or open bracket (‘[‘), push it onto the character stack.
3 . Whenever any close bracket (‘]’) is encounter pop the character from the character stack until open bracket (‘[‘) is not found in the character stack. 
4. Also, pop the top element from the integer stack, say n. Now make a string repeating the popped character n number of time. 
5. Now, push all character of the string in the stack.


'''


def isNumber(ch):
    try:
        int(ch)
        return True
    except:
        return False
    

def decodeString(arr):
    nums = []
    stack = []
    temp = ""
    i = 0
    while i < len(arr):
        
        # This section is to check if its a number 
        if arr[i].isdigit():
            repeat_time = 0
            
            # Number can be 2 digit as well
            while arr[i].isdigit():
                repeat_time = 10 * repeat_time + int(arr[i])
                i = i + 1
                
            # we need this one because we went one bit far , come back and start from previous bit    
            i = i - 1    
            nums.append(repeat_time)
            
        elif arr[i] == "]":
            temp = ""
            # pop elements till we get [ from stack
            while len(stack) > 0:
                popped_element = stack.pop()
                if popped_element == "[":
                    break
                temp = popped_element + temp 
            
            temp = nums.pop() * temp
            stack.append(temp)
        else:
            stack.append(arr[i])  
        i = i + 1    
    
    print(temp)


    # pass
if __name__ == '__main__':
    str = "1[b]"
    str = "2[ab]"
    str = "3[b2[ca]]"
    #str = "10[a]"
    str = list(str)
    decodeString(str)
    
