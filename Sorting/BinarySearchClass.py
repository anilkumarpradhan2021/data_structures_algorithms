'''
Created on 19-May-2016

@author: anpradha
'''

def binarySearch(arr, val):
    low = 0;
    high = len(arr) -1
    while(low <= high and high < len(arr)):
        mid = int((low + high) / 2)
        if(arr[mid] == val):
            return mid
        elif(arr[mid] > val):
            high = mid - 1
        elif(arr[mid] < val):
            low = mid + 1
    return -1        

def binary(arr,num):
	low = 0
	high = len(arr) -1
	
	while low <= high and high<len(arr):
		mid = (low + high) // 2
		if arr[mid] == num:
			return True
		elif arr[mid] > num:
			high = mid -1
		else:
			low = mid + 1
	return False		

def binaryRecurssionSearch(arr, val, low, high):
    if(low <= high):
        mid = int((low + high) / 2)
        if(arr[mid] == val):
            return mid
        elif(arr[mid] > val):
            return binaryRecurssionSearch(arr, val, low, mid - 1)
        elif(arr[mid] < val):
            return binaryRecurssionSearch(arr, val, mid + 1, high)
    return -1   
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(binarySearch(arr, 8))
    #print(binaryRecurssionSearch(arr, 8, 0, len(arr) - 1))
    print(binary(arr,-1))
    
