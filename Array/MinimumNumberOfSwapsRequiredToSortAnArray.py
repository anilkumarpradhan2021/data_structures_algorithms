'''
Created on 24-Jul-2019

@author: anpradha



Minimum number of swaps required to sort an array
Given an array of n distinct elements, find the minimum number of swaps required to sort the array.

Examples:

Input : {4, 3, 2, 1}
Output : 2
Explanation : Swap index 0 with 3 and 1 with 2 to 
              form the sorted array {1, 2, 3, 4}.

Input : {1, 5, 4, 3, 2}
Output : 2


Check this video for understanding:
https://www.youtube.com/watch?v=f7IIW0HVUcQ


'''


def minSwaps(arr): 
    n = len(arr) 
      
    # Create two arrays and use as pairs where first array is element and second array is position of first element 
    arrpos = [*enumerate(arr)] 
    print("Array print with index and corresponding element")
    print(arrpos)
      
    # Sort the array by array element  
    # values to get right position of  
    # every element as the elements  
    # of second array. 
    print("Sorted array based on element value ")
    arrpos.sort(key=lambda it:it[1]) 
    print(arrpos)
      
    # To keep track of visited_flagited elements.  
    # Initialize all elements as not visited_flagited or False. 
    visited_flag = {k:False for k in range(n)} 
      
    # Initialize result 
    ans = 0
    for index in range(n): 
          
        # already swapped or already present at correct position 
        if visited_flag[index] or arrpos[index][0] == index: 
            continue
              
        # find number of nodes in this cycle and  add it to ans 
        no_of_nodes_in_cycle = 0
        j = index 
        while not visited_flag[j]: 
              
            # mark node as visited_flagited 
            visited_flag[j] = True
              
            # move to next node 
            j = arrpos[j][0] 
            no_of_nodes_in_cycle = no_of_nodes_in_cycle + 1
              
        # update answer by adding current cycle , 
        ''' for any cycle the maximum number of swap to fix the position of all element is number nodes in cycle -1 e.g 1 -- > 2 -->1 , then we need  2-1 = 1 swap '''
        if no_of_nodes_in_cycle > 0: 
            print("no_of_nodes_in_cycle " ,no_of_nodes_in_cycle)
            ans = ans + (no_of_nodes_in_cycle - 1) 
    # return answer 
    return ans 

  
# Driver Code      

if __name__ == '__main__':
    arr = [1, 5, 4, 3, 2] 
    print(minSwaps(arr)) 
