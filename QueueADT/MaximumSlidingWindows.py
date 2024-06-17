'''
Created on 03-Jul-2016

@author: anpradha

Sliding Window Maximum (Maximum of all subarrays of size k)
Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.
Examples :

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
Output: 3 3 4 5 5 5 6

Time Complexity: Time Complexity of steps 4(a) is O(k), 4(b) is O(Log(k)) and it is in a loop that runs (n – k + 1) times. 
Hence, the time complexity of the complete algorithm is O((k + Log(k)) * n) 

i.e. O(n * k).

1 . Pick first k elements and create a max heap of size k.
2. Perform heapify and print the root element.
3. Store the next and last element from the array
4. Run a loop from k – 1 to n
    4.1Replace the value of element which is got out of the window with new element which came inside the window.
    4.2 Perform heapify.
    4.3Print the root of the Heap.


https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/



'''

import heapq


def findMaximumFromWindowSize(arr, k):
    
    ''' create a max heap with k element'''
    temp = arr[:k]
    heapq._heapify_max(temp)
    for i in range(k, (len(arr))):
        max_k = heapq.heappop(temp)
        print(max_k)
        heapq.heappush(temp, arr[i])
        heapq._heapify_max(temp)
        
        if i == len(arr) - 1:
            max_k = heapq.heappop(temp)
            print(max_k,end= " ")
    
    print("\n------------------------------")

''' 
    deque means dobule ended queue , it means we can add / delete from both side
    complexity O(n)
    
    Simple steps
    1. remove all elements from deque if current is >= to all other element
    2. else add current to add / rear 
    3. check for window size , if old index i.e is not applicable for this current window then remove it. 

Time Complexity: O(n). It seems more than O(n) at first look. 
If we take a closer look, we can observe that every element of array is added and removed at most once. So there are total 2n operations.
Auxiliary Space: O(k)




'''
from collections import deque


def findMaximumFromWindowSizeUsingDeque(arr, k):
    q = deque()
    
    for i in range(k):
        if len(q) > 0 and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)  
    
    for i in range(k, len(arr)):

        print(arr[q[0]],end=" ")    

        ''' if the window size of q is in range that is k'''
        while len(q) > 0 and q[0] <= i - k:
            q.popleft()
        
        ''' check if the last element is less than present , if yes delete it'''
        while len(q) > 0 and  arr[i] >= arr[q[-1]]:
            q.pop()          
        
        q.append(i)
    print(str(arr[q[0]])) 


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    window = 3
    findMaximumFromWindowSize(arr, window)
    findMaximumFromWindowSizeUsingDeque(arr, window)
