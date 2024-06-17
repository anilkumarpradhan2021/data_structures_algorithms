'''
Created on 23-Nov-2019

@author: anpradha

Search in an array of strings where non-empty strings are sorted
Given an array of strings. The array has both empty and non-empty strings. All non-empty strings are in sorted order. Empty strings can be present anywhere between non-empty strings.

Examples:

Input :  arr[] =  {"for", "", "", "", "geeks", 
                   "ide", "", "practice", "" , 
                   "", "quiz", "", ""};
          str = "quiz"
Output :   10
The string "quiz" is present at index 10 in 
given array.



'''


def searchStr2(arr, string, low, high):
    if low < high:
        mid = (low + high) // 2
        # check if mid is "" 
        if len(arr[mid]) == 0:
            i = mid - 1 
            j = mid + 1
            while i < j and i > low and j < high:
                if i > low and len(arr[i]) != 0:
                    mid = i
                    break
                if j < high and len(arr[j]) != 0:
                    mid = j 
                    break
                i = i - 1
                j = j + 1
        
        if arr[mid] == string:
            return mid
        if arr[mid] > string:
            return searchStr2(arr, string, low, mid - 1)
        if arr[mid] < string:
            return searchStr2(arr, string, mid + 1, high)
    return -1    
        

def searchStr(arr, string, first, last): 
   
    if first > last: 
        return -1 
  
    # Move mid to the middle  
    mid = (last + first) // 2 
  
    # If mid is empty , find closet non-empty string  
    if len(arr[mid]) == 0: 
        # If mid is empty, search in both sides of mid  
        # and find the closest non-empty string, and  
        # set mid accordingly.  
        left = mid - 1
        right = mid + 1 
        while True: 
           
            if left < first and right > last: 
                return -1
                  
            if right <= last and len(arr[right]) != 0: 
                mid = right  
                break 
               
            if left >= first and len(arr[left]) != 0: 
                mid = left  
                break 
               
            right = right + 1 
            left = left - 1
  
    # If str is found at mid  
    if string == arr[mid]: 
        return mid  
  
    # If str is greater than mid  
    if string > arr[mid]: 
        return searchStr(arr, string, mid + 1, last)  
  
    # If str is smaller than mid  
    return searchStr(arr, string, first, mid - 1)  


if __name__ == '__main__':
    arr = ["for", "", "", "", "geeks", "ide", "",
                    "practice", "" , "", "quiz", "", ""]  
  
    # input Search String  
    string = "quiz" 
    n = len(arr)  
    print(searchStr(arr, string, 0, n - 1))  
    print(searchStr2(arr, string, 0, n - 1))  

