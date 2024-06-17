'''
Created on 19-Oct-2019

@author: anpradha


Find the point where maximum intervals overlap

Consider a big party where a log register for guest’s entry and exit times is maintained. Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.

Example :

Input: arrl[] = {1, 2, 9, 5, 5}
       exit[] = {4, 5, 12, 9, 12}
First guest in array arrives at 1 and leaves at 4, 
second guest arrives at 2 and leaves at 5, and so on.

Output: 5
There are maximum 3 guests at time 5.  


Another Efficient Solution :
Approach :
1). Create an auxiliary array used for storing dynamic data of starting and ending points.

2). Loop through the whole array of elements and increase the value at the starting point by 1 and similarly decrease the value after ending point by 1.
[Here we use the expressions “x[start[i]]-=1” and “x[end[i]+1]-=1”]

3). While looping, after calculating the auxiliary array: permanently add the value at current index and check for the maximum valued index traversing from left to right.



'''


def maxOverlap(start, end): 
   
    n = len(start) 
    maxa = max(start)  # Finding maximum starting time 
    maxb = max(end)  # Finding maximum ending time 
    maxc = max(maxa, maxb) 
    
    ''' +2 is because the array should be from 0 to maxvalue , including maxValue'''
    x = (maxc + 2) * [0] 
   
    for i in range(0, n) :  # CREATING AN AUXILIARY ARRAY 
        x[start[i]] = x[start[i]] + 1  # Lazy addition 
        
        # +1 because for that hour exit person will be considered
        x[end[i] + 1] = x[end[i] + 1] - 1
    
    maxy = -1
    cur = 0
    idx = 0
    # Lazily Calculating value at index i 
    for i in range(0, maxc + 1):  
        cur = cur + x[i] 
        if maxy < cur : 
            maxy = cur 
            idx = i      
    print("Maximum value is: {0:d}".format(maxy),
                     " at position: {0:d}".format(idx)) 


if __name__ == "__main__": 
       
    start = [13, 28, 29, 14, 40, 17, 3] 
    end = [107, 95, 111, 105, 70, 127, 74] 
                     
    maxOverlap(start, end) 
