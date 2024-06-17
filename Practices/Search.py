'''
Created on 04-Jul-2017

@author: anpradha
'''


def linearSearch(number, arr):
    for i in arr:
        if number == i:
            return True
    return False    


def binarySearch(number, arr):
    low = 0    
    high = len(arr) - 1 
    
    while low <= high :
        mid = (low + high) // 2
        if arr[mid] == number :
            return True
        elif arr[mid] > number :
            high = mid - 1
        else:
            low = mid + 1
    return False            


def partition(arr, low, high):
        pivot = low
        i = low
        j = high

        while i < j :
            while i < high and arr[i] <= arr[pivot]:
                i = i + 1
                
            while j > low and arr[j] > arr[pivot]:
                j = j - 1
    
            if i < j:
                ''' Swap '''
                arr[i] , arr[j] = arr[j], arr[i]
        
        arr[j] , arr[pivot] = arr[pivot], arr[j]
        return j


def findKthSmallestElement(arr , position, left, right):
    if position >= left and position <= right:
        pivot = partition(arr, left, right)
        print("pivot : " , pivot)
        print("position : " , position)
        if position == pivot:
            return arr[pivot]
        elif position < pivot:
            return findKthSmallestElement(arr, position, left, pivot - 1)
        else:
            return findKthSmallestElement(arr, position, pivot + 1, right)
    
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    number = 8
    # print(linearSearch(number, arr))
    # print(binarySearch(number, arr))
    print(findKthSmallestElement(arr, 5, 0, (len(arr) - 1)))
