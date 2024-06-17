'''
Created on 03-Sep-2016

@author: anpradha
'''



'''
Following is the algorithm for finding the next greater number.
I) Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. 
For example, 
if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. 
If we do not find such a digit, then output is “Not Possible”.

II) Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. 
For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.

III) Swap the above found two digits, we get 536974 in above example.

IV) Now sort all digits from position next to ‘d’ to the end of number. 
The number that we get after sorting is the output. For above example, 
we sort digits in bold 536974. We get “536479” which is the next greater number for input 534976.
'''


def find_next_number(arr):
        
    '''
      I) Start from the right most digit and find the first digit that is smaller than the digit next to it.
    '''
    i = len(arr) - 1
    while i > 0 :
        if arr[i] > arr[i - 1]:
            break
        i = i - 1
    
    '''
    If no such digit is found, then all digits are in descending order 
    means there cannot be a greater number with same set of digits
    '''
    if i == 0 :
        print("Smaller number not possible")
        return 
    
    ''' 
    II) Find the smallest digit on right side of (i-1)'th digit that is greater than number[i-1] 
    '''

    x = arr[i - 1]
    smallest = i; 
    j = i 
    while j < len(arr):
        if arr[j] > x and arr[j] < arr[smallest]:
            smallest = j
        j = j + 1    
    
    
    '''
    III) Swap the above found smallest digit with number[i-1]
    '''
    arr[i - 1], arr[smallest] = arr[smallest], arr[i - 1]
    
    '''
    IV) Sort the digits after (i-1) in ascending order
    '''
    a = list(sorted(arr[i :]))
    arr = arr[:i ] + a
    # print(arr)
    return arr

if __name__ == '__main__':
    arr = list("534976")
    print("\nPrevious Number : " + str(arr))
    print("Next Number : " + str(find_next_number(arr)))
    
    arr = list("218765")
    print("\nPrevious Number : " + str(arr))
    print("Next Number : " + str(find_next_number(arr)))

    arr = list("1234")
    print("\nPrevious Number : " + str(arr))
    print("Next Number : " + str(find_next_number(arr)))

    arr = list("4321")
    print("\nPrevious Number : " + str(arr))
    print("Next Number : " + str(find_next_number(arr)))

            
                 
        
        
