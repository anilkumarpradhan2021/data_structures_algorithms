'''
Created on 02-Aug-2016

@author: anpradha


The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that 
all elements of the subsequence are sorted in increasing order. 

For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

Time complexity of the above Dynamic Programming (DP) solution is O(n^2) 

'''

# L(i) = { 1 + Max ( L(j) ) } where j < i and arr[j] < arr[i] and if there is no such j then L(i) = 1
if __name__ == '__main__':
    arry = [ 10, 22, 9, 33, 21, 50, 41, 60, 80]
    print("array : " , arry)
    
    # Create a array to store all previous value 
    # Initialize LIS values for all indexes
    lis = [1] * len(arry)

    for i in range(len(arry)):
        for j in range(0, i):
            if arry[j] < arry[i] and lis[i] < 1 + lis[j]:
                    lis[i] = lis[j] + 1
                    
    print("lis : ",  lis)                
    number_of_sequence = 0
    end_index = 0
    for i in range(len(lis)):
        if lis[i] > number_of_sequence:
            number_of_sequence = lis[i]
            end_index = i
    
    print("Longest Increasing Sequence :" + str(number_of_sequence))  
    print("Longest Increasing Sequence end index:" + str(end_index))  
    print(lis)
    s = len(lis) - 1
    while s >= 0:
        if lis[s] == number_of_sequence :
            print(arry[s], end=' ')
            number_of_sequence = number_of_sequence - 1
        
        s = s - 1    

      
                            
