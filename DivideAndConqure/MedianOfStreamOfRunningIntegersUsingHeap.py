'''
Created on 13-Oct-2019

@author: anpradha


Median of Stream of Running Integers using STL

Given that integers are being read from a data stream. Find median of all the elements read so far starting from the first integer till the last integer. This is also called Median of Running Integers. The data stream can be any source of data, example: a file, an array of integers, input stream etc.


What is Median?

Median can be defined as the element in the data set which separates the higher half of the data sample from the lower half.
 In other words we can get the median element as, when the input size is odd, we take the middle element of sorted data.
If the input size is even, we pick average of middle two elements in sorted stream.

Example:

Input: 5 10 15
Output: 5
        7.5
        10
Algorithm:

Very Simple:
1. Assign median as arr[0]
2. create max and min heap
3. always remember elements in max heap == min heap or max heap + 1 = min heap
4. so if size of max and min same then median is max[0] + min[0] // 2
5. if max heap size + 1 = min heap then median is max[0]
6. if incoming element is < previous median then add to max heap else add it to min heap


When a new value arrives, it is placed in the maxHeap if the value is less than or equal to the median, 
otherwise 
    it is placed into the min Heap. The heap sizes can be equal, or the maxHeap may have one extra element. 
Note: This constraint can easily be restored by shifting an element from

one heap to the other. The median is available in constant time, by looking at the top element(s). Updates
takeO(log(n)) time

Important:
we dont have max heap in python we need to override some methods : easy is store the value with -1 * element
'''

import heapq


def medianOfStream(arr):
    # Take initial value of median as 0.
    median = arr[0]
    
    # max heap to store the smaller half elements  
    maxheap = []
    heapq.heapify(maxheap)
    
    # min heap to store the greater half elements  
    minheap = []    
    heapq.heapify(minheap)
    
    for element in arr:
        if len(minheap) == len(maxheap) :
            if element <= median:
                heapq.heappush(maxheap, -1 * element)
            else:
                minheapPop = heapq.heappop(minheap)
                # push to max heap
                heapq.heappush(maxheap, -1 * minheapPop)

                # push the element to minheap
                heapq.heappush(minheap, element)
                
            median = -1 * maxheap[0] 
            
        elif len(maxheap) > len(minheap) :
            if element <= median:
                maxheapPop = heapq.heappop(maxheap)

                # push to min heap
                heapq.heappush(minheap, -1 * maxheapPop)
                
                # push the element to maxheap
                heapq.heappush(maxheap, -1 * element)
                median = -1 * maxheap[0] 
       
            else:
                # push to min heap
                heapq.heappush(minheap, element)
                    
                median = (minheap[0] + (-1 * maxheap[0])) / 2
            
        print("median: " , median)    
        # print("maxheap : "  , maxheap)
        # print("minheap " , minheap)


if __name__ == '__main__':
    arr = [5, 10, 15]
    arr = [5, 15, 10, 20, 3]
    medianOfStream(arr)
