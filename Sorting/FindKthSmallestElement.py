'''
Created on 29-May-2017

@author: anpradha

K’th Smallest/Largest Element in Unsorted Array | Set 1
Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that ll array elements are distinct.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 4
Output: 10


Method 4 (QuickSelect)
This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step. In QuickSort, 
we pick a pivot element, then move the pivot element to its correct position and partition the array around it. 

The idea is, not to do complete quicksort, but stop at the point where pivot itself is k’th smallest element. 
Also, not to recur for both left and right sides of pivot, but recur for one of them according to the position of pivot. 
The worst case time complexity of this method is O(n2), but it works in O(n) on average.

'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.arr = [12, 23, 1, 24, 111, 34, 2]
        
    
    def print(self):
        print("Print array before sort")
        print(self.arr)
        print(self.findKthSmallestElement(5, 0, len(self.arr) - 1))
        self.quickSort(0, len(self.arr) - 1)
        print(self.arr)
        
    def partition(self, low, high):
            pivot = low
            i = low
            j = high

            while i < j :
                while i < high and self.arr[i] <= self.arr[pivot]:
                    i = i + 1
                    
                while j > low and self.arr[j] > self.arr[pivot]:
                    j = j - 1
        
                if i < j:
                    ''' Swap '''
                    self.arr[i] , self.arr[j] = self.arr[j], self.arr[i]
            
            self.arr[j] , self.arr[pivot] = self.arr[pivot], self.arr[j]
            return j


    def findKthSmallestElement(self, position, left, right):
        if position >= left and position < right:
            pivot = self.partition(left, right)
            print("pivot : " , pivot)
            print("(left + pivot + 1) : " + str((left + pivot + 1)))
            if position == (left + pivot + 1):
                return position
            elif position > (left + pivot + 1):
                return self.findKthSmallestElement(position, left, pivot - 1)
            else:
                return self.findKthSmallestElement(position, pivot + 1, right)
    
    def quickSort(self, left, right):
        if left < right :
            pivot = self.partition(left, right)
            self.quickSort(left, pivot - 1)
            self.quickSort(pivot + 1 , right)
            
            

'''
updated on 01/10/2019

'''
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
            
                       
        
if __name__ == "__main__":
    a = MyClass()
    a.print()
    arr = [11, 22, 3, 4, 35, 6, 72, 8]
    print(findKthSmallestElement(arr, 5, 0, (len(arr) - 1)))
    print(sorted(arr))

    
         
