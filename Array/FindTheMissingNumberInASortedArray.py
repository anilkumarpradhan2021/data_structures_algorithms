'''
Created on 19-Sep-2019

@author: anpradha


Find the Missing Number in a sorted array
Given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

Examples:

Input : arr[] = [1, 2, 3, 4, 6, 7, 8]
Output : 5

Input : arr[] = [1, 2, 3, 4, 5, 6, 8, 9]
Output : 7



'''


def findTheMissinggElement(arr):
    left_index = 0
    right_index = len(arr) - 1
    
    '''Very min. condition is left , element , right , assume left < right and left is 3 and high is 4 , then no element between then , then why to continue '''
    while left_index + 1 < right_index:
        mid_index = (left_index + right_index) // 2
        print("left : " , left_index , "right : " , right_index , "mid : " , mid_index)
        
        if (arr[left_index] - left_index) != (arr[mid_index] - mid_index):
            right_index = mid_index 
        elif (arr[right_index] - right_index) != (arr[mid_index] - mid_index): 
            left_index = mid_index

    return arr[mid_index] + 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 8] 
    print(findTheMissinggElement(arr))
