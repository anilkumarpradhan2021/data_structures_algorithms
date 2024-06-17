'''
Created on 10-May-2016

@author: anpradha

Variation	    Time Complexity	    Space Complexity
Best Case	    O(n log n)	        O(log n)
Average Case	O(n log n)	        O(log n)
Worst Case	    O(n^2)	            O(n)
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.arr = [12, 23, 1, 24, 111, 34, 1, 12, 2 ]
        
    
    def print(self):
        print("Print array before sort")
        print(self.arr)
        self.quickSort(0, len(self.arr) - 1)
        print("Print array after sort")
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

   
    def quickSort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.quickSort(low, pivot - 1)
            self.quickSort(pivot + 1, high)
               
        
if __name__ == "__main__":
    a = MyClass()
    a.print()

    
         
