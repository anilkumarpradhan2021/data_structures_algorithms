'''
Created on 13-Oct-2016

@author: anpradha
Problem :
Objec­tive: Rearrange Pos­i­tive and Neg­a­tive Num­bers of an Array so that one side you have pos­i­tive num­bers and other 
side with neg­a­tive Inte­gers with­out chang­ing their respec­tive order.

Example : 
Input :  1 -2 3 -4 5 -6 7 -8 9 -10
ReArranged Output :  -2 -4 -6 -8 -10 1 3 5 7 9

Use Quick sort technique.

    Take the pivot ele­ment as 0 and do the first round of Quick Sort.
    After above step you will have all the neg­a­tive ele­ments on left and all the pos­i­tive ele­ments on the right.

Time Com­plex­ity : O(n) Space Com­plex­ity: O(1)

'''

def arrageNumber(arr):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        while arr[low] < 0 :
            low = low + 1

        while arr[high] > 0   :
            high = high - 1
            
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]    
            
    print(arr)


if __name__ == '__main__':
    arr = [1 , -2 , 3 , -4, 5, -6, 7, -8, 9 , -10]
    arrageNumber(arr)

    arr = [1 , 2 , 3 , 4, -5, -6, 7, -8, 9 , -10]
    arrageNumber(arr)
