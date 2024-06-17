'''
Created on 13-Oct-2016

@author: anpradha

Problem :
Objec­tive: Given an array arrA[] which has neg­a­tive and pos­i­tive ele­ments, rearrange the array in such a man­ner 
that pos­i­tive and neg­a­tive ele­ments occupy the alter­nate posi­tions and if there are extra pos­i­tive or neg­a­tive ele­ments 
are left then append it to the end.

e.g
int[] arrA = { 1, 2, -3, -4, -5, 6, -7, -8, 9, 10, -11, -12, -13, 14 };
Output: -13 9 -3 10 -5 6 -7 2 -12 1 -11 14 -4 -8


Use Quick sort technique.

    Take the pivot ele­ment as 0 and do the first round of Quick Sort.
    After above step you will have all the neg­a­tive ele­ments on left and all the pos­i­tive ele­ments on the right.

    Then just the every alter­nate ele­ment in the left half (neg­a­tive ele­ments) with the ele­ments in the right (pos­i­tive elements)

Time Com­plex­ity : O(n) Space Com­plex­ity: O(1)

'''


def arragePositiveAndNegativeNumberAlternatively(arr):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        while arr[low] < 0 :
            low = low + 1

        while arr[high] > 0   :
            high = high - 1
            
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]    
    
    
    ''' find the starting point for +ve number'''
    postitive_start_pos = 0        
    for i in arr:
        if i < 0 :
            postitive_start_pos = postitive_start_pos + 1        
    
    i = 1
    while arr[i] < 0 and postitive_start_pos < len(arr):
        arr[i], arr[postitive_start_pos] = arr[postitive_start_pos], arr[i]  
        i = i + 2
        postitive_start_pos = postitive_start_pos + 1
                      
    print(arr)

if __name__ == '__main__':
    
    arr = [1 , 2 , 3 , 4, -5, -6, 7, -8, 9 , -10]
    print(arr)
    arragePositiveAndNegativeNumberAlternatively(arr)
