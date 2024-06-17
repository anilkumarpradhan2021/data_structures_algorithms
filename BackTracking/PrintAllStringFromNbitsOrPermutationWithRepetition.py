'''
Created on 19-Sep-2016

@author: anpradha
'''

'''
Gen­er­ate All Strings of n bits, con­sider A[0..n-1] is an array of size n.]

Exam­ple :

n = 3
Output:
[0, 0, 0]    [1, 0, 0]    [0, 1, 0]    [1, 1, 0]

[0, 0, 1]     [1, 0, 1]     [0, 1, 1]    [1, 1, 1]


'''


def generate_all(arr, n):
    ''' Base case: n is 0, print arr '''
    if n == 0:
        print(arr)
    else:
        arr[n - 1] = 0
        generate_all(arr, n - 1)
        arr[n - 1] = 1
        generate_all(arr, n - 1)


''' 
Print all possible strings of length k that can be formed from a set of n characters

Given a set of characters and a positive integer k, print all possible strings of length k that can be formed from the given set.

Examples:

Input: 
set[] = {'a', 'b'}, k = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb


Input: 
set[] = {'a', 'b', 'c', 'd'}, k = 1
Output:
a
b
c
d
'''


def generic_generate_all(arr, temp , k):
    
    ''' Base case: k is 0, print temp '''
    if k == 0:
        print(temp)
    else:
        ''' One by one add all characters from set to temp and decrease index of temp and recursively call for k equals to k-1'''
        for i in range(len(arr)):
            temp[k - 1] = arr[i]
            ''' k is decreased, because we have added a new character from arr to temmp '''
            generic_generate_all(arr, temp, k - 1)

            
if __name__ == '__main__':
    arr = ['A' , 'B' , 'C']
    arr = [1, 0]
    # arr = [0, 1]
    k = 3
    temp = [0 for i in range(k)]
    # generate_all(arr, len(arr))  # arr = [0,1]
    generic_generate_all(arr, temp, k)
    
