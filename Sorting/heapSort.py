'''
Created on 26-Oct-2019

@author: anpradha

Time Complexity: Time complexity of heapify is O(Logn).
Time complexity of createAndBuildHeap() is O(n) and overall time complexity of Heap Sort is O(nLogn).

https://www.geeksforgeeks.org/heap-sort/

heap sort approach is similar to selection sort , means select a element compare with all other and found the max/min in 1st 
iteration , same approach for next and so on. 

Heapfiy should be done from bottom t0 top , means child must be fixed 1st then fix the parent.
Because of this we as the root is position at 0 index , so we start from child i.e from end

'''


def heafify(arr, size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    
    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size  and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest] , arr[i] = arr[i] , arr[largest]
        heafify(arr, size, largest)


def heapSort(arr):
    size = len(arr)
    for i in range(len(arr) // 2 , -1, -1):
        heafify(arr, size, i)            
    
    print("Max heap is done now , the 0th element contain the highest value, For sorted o/p , we need to replace the 0th element with size -1 th element and so on.")
    print(arr)
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heafify(arr, i, 0)        


if __name__ == '__main__':
    print("array before sort")
    arr = [ 1, 11, 13, 5, 6, 2]
    print(arr)

    heapSort(arr) 
    print("array After sort")
    print(arr)
    
