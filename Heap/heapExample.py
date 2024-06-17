'''
Created on 31-Aug-2016

@author: anpradha
'''


# heap implementation using Array 
'''
when i start from 1 
For Node at i 
Left Child is 2i
Right Child 2i + 1

if node is at i then root is i // 2

when i start from 0 
For Node at i 
Left Child is 2i +1
Right Child 2i + 2

if node is at i then root is i -1 // 2


Max heap  = root having the maximum Value 
Min heap  = root having minimum value 

Import Point learnt : 
immutable :  integers, strings or tuples
mutable : List

'''

def max_heapify(arr, i, arr_length):
    left_child_index = 2 * i
    right_child_index = 2 * i + 1
    largest_element_index = i
    
    if left_child_index < arr_length and arr[left_child_index] > arr[i] : 
        largest_element_index = left_child_index
        
    if right_child_index < arr_length and arr[right_child_index] > arr[largest_element_index] : 
        largest_element_index = right_child_index
    
    if largest_element_index != i:
        temp = arr[largest_element_index]
        arr[largest_element_index] = arr[i]
        arr[i] = temp


def build_max_heap(arr):
    # From leaf to Root
    for i in range(int(len(arr) / 2) + 1, 0, -1):
        max_heapify(arr, i, len(arr))
        
def heap_sort(arr):
    build_max_heap(arr)
    heap_size = len(arr) - 1 
    for i in range(1, len(arr)):
        print(arr[1], end=" ")
        
        ''' Replace the last element with 1st element and then heapify 
        '''
        arr[1] = arr[heap_size]
        heap_size = heap_size - 1
        max_heapify(arr, 1, heap_size)

def increase_value(arr, val, position):
    if arr[position] < val:
        arr[position] = val
        
        while position > 1 and arr[int(position / 2)] < arr[position]:
            temp = arr[int(position / 2)]
            arr[int(position / 2)] = arr[position]
            arr[position] = temp
            position = int(position / 2) 
    print(arr)        
             
def insert_queue(arr, val):
    arr.append(-1)  # assuming all values are greater than 0
    increase_value(arr, val, len(arr) - 1)

def extract_maximum(arr, queue_size):
    if queue_size <= 0:
        print("queue is empty")
        return
            
    print("Maximum :" + str(arr[1]))
    arr[1] = arr[queue_size]
    max_heapify(arr, 1, queue_size - 1)
    

'''Biggest learning '''
        
def swap(i, j):
    temp = i
    i = j
    j = temp    
    
if __name__ == '__main__':
    pass
    a = [0, 1, 4, 3, 7, 8, 9, 10]
    print("Before Heap Sort")
    print(a)
    print("After heap sort")
    heap_sort(a)  
    
    priority_queue = [0]
    insert_queue(priority_queue, 1)
    insert_queue(priority_queue, 4)
    insert_queue(priority_queue, 3)
    insert_queue(priority_queue, 7)
    insert_queue(priority_queue, 8)
    insert_queue(priority_queue, 9)
    insert_queue(priority_queue, 10)
    queue_size = len(priority_queue) - 1 
    extract_maximum(priority_queue, queue_size)
    queue_size = queue_size - 1
    extract_maximum(priority_queue, queue_size)
    
    
