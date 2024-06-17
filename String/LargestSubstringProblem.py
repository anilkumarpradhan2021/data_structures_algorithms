'''
Created on 01-Sep-2016

@author: anpradha

https://www.youtube.com/watch?v=BysNXJHzCEs


'''


def print_array(arr):
    print()    

    #  X Represent Number of rows
    for x in range(len(arr)):
        # Y represent Number of Column
        for y in range(len(arr[0])):
            # print(" x : " + str(x) + " y : " + str(y) , end= " ")
            print(arr[x][y] , end=" ")
        print()    


def largestPalindromUsingDP(string1, string2):
    # Create 2 dimentional array depending on the string1 and string2 length 
    arr = [[0 for x in range(len(string1) + 1)] for y in range(len(string2) + 1)]
    print_array(arr)
    
    maximum_sub_string_length = 0
    maximum_sub_string_i = 0
    maximum_sub_string_j = 0
    for i in range(1, len(string2) + 1):
        for j in range(1, len(string1) + 1):
            # print(" x : " + str(i) + " y : " + str(j) , end= " ")
            if string2[i - 1] == string1[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
                
                # Calculate the maximum substring length and track the index 
                if maximum_sub_string_length < arr[i][j]:
                    maximum_sub_string_length = arr[i][j] 
                    maximum_sub_string_i = i
                    maximum_sub_string_j = j
    
    print("Updated Matrix")            
    print_array(arr)
    # Substring length 
    print("Maximum Substring length  : " + str(maximum_sub_string_length))
    print("maximum_sub_string_i  : " + str(maximum_sub_string_i))
    print("maximum_sub_string_j  : " + str(maximum_sub_string_j))
    
    # Choosing the largest String
    starting_index = maximum_sub_string_i - maximum_sub_string_length
    while starting_index < maximum_sub_string_i:
        print(string2[starting_index], end=" ")
        starting_index = starting_index + 1

        
if __name__ == '__main__':
    pass
    string1 = "tutorialhorizon"
    string2 = "dynamictutorialProgramming"
    print("string1 : " + string1)
    print("string2 : " + string2)

    string1 = "abcdef"
    string2 = "abc"
    print("string1 : " + string1)
    print("string2 : " + string2)
    
    largestPalindromUsingDP(string1, string2)
