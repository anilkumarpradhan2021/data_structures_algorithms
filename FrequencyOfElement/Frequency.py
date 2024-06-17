'''
Created on 01-Jun-2016

@author: anpradha


Count frequencies of all elements in array in O(1) extra space and O(n) time

Given an unsorted array of n integers which can contain integers from 1 to n. Some elements can be repeated multiple times and some other elements can be absent from the array. Count frequency of all elements that are present and print the missing elements.

Examples:

Input: arr[] = {2, 3, 3, 2, 5}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 2
        3 -> 2
        4 -> 0
        5 -> 1

Input: arr[] = {4, 4, 4, 4}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 0
        3 -> 0
        4 -> 4
        
        
'''


def frequencyOfElement(arr):
    pos = 0;
    while(pos < len(arr)):
        expected_pos = arr[pos] - 1
        if(arr[pos] > 0 and arr[expected_pos] > 0):
            temp = arr[pos]
            arr[pos] = arr[expected_pos]
            arr[expected_pos] = temp
            arr[expected_pos] = -1
        elif(arr[pos] > 0):
            arr[expected_pos] = arr[expected_pos] - 1
            arr[pos] = 0
            pos = pos + 1
        else:
            pos = pos + 1    
    for i in range(0, len(arr) - 1):
        print(abs(arr[i]))


'''
Method 2 (By adding n to keep track of counts)

1)  Subtract 1 from every element so that the elements
    become in range from 0 to n-1
    for (int j =0; j < n; j++)
        arr[j] = arr[j]-1;

2)  Use every element arr[i] as index and add 'n' to
    element present at arr[i]%n to keep track of count of
    occurrences of arr[i]
    for (int i=0; i < n; i++)
        arr[arr[i]%n] = arr[arr[i]%n] + n;

3)  To print counts, simply print the number of times n
    was added at index corresponding to every element
    for (int i =0; i < n; i++)
        print "(i + 1) -> arr[i] " 
 
 https://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/       
        
'''


def frequencyOfElementSimple(arr):
    
    ''' As  the condition is its a range bound that is from 1 to n '''
    ''' substract 1 from each element in arr so that each will fit to there actual index '''

    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] - 1    

    '''   Use every element arr[i] as index and add 'n' to element present at arr[i]%n to keep track of count of occurrences of arr[i]  
     '''
    for i in range(n):
        arr[ arr[i] % n] = arr[ arr[i] % n] + n
    
    '''# To print counts, simply print the  
        # number of times n was added at index  
        # corresponding to every element  '''
    for i in range(n): 
        print(i + 1, "->", arr[i] // n)  
    

        
if __name__ == '__main__':
    arr = [1, 2, 4, 5, 6, 6, 6]
    frequencyOfElement(arr)
    arr = [1, 2, 4, 5, 6, 6, 6]
    arr = [4,4,4,4]
    frequencyOfElementSimple(arr)
    
