'''
Created on 26-Aug-2019

@author: anpradha


The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence 
such that all elements of the subsequence are sorted in increasing order. 

For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

More Examples:

Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}

Video:
https://www.youtube.com/watch?v=CE2b_-XfVDk

Dynamic Programming (DP) solution is O(n^2)

'''

if __name__ == '__main__':
    arr = [3, 4, -1, 0, 6, 2, 3]
    
    # Declare the temp (array) for  storing the initial count for . 
    temp = [1] * len(arr)
    print(temp)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                temp[i] = max(temp[i], temp[j] + 1)
    
    print(temp)
    # get the maximum value from the temp
    print(max(temp))            
             
