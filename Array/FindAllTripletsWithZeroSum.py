'''
Created on 22-Nov-2019

@author: anpradha

Find all triplets with zero sum
Given an array of distinct elements. The task is to find triplets in array whose sum is zero.

Examples :

Input : arr[] = {0, -1, 2, -3, 1}
Output : 0 -1 1
         2 -3 1

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1

Time Complexity : O(n2)
Auxiliary Space : O(n)




'''


def findTripletsWithSumZero(arr):
    for i in range(len(arr)):
        d = {}

        for j in range(i + 1, len(arr)):
            if -(arr[i] + arr[j]) in d:
                print(arr[i] , arr[j] , -(arr[i] + arr[j]))
            else:
                d[arr[j]] = arr[j]
            print(d)    
    
def findTriplets(arr, n): 
    found = False
    for i in range(n - 1): 
  
        # Find all pairs with sum  
        # equals to "-arr[i]"  
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                print(x, arr[i], arr[j]) 
                found = True
            else: 
                s.add(arr[j]) 
    if found == False: 
        print("No Triplet Found") 


if __name__ == '__main__':
    arr = [-1, 1, 2, -3, 0]
    findTripletsWithSumZero(arr)
    # findTriplets(arr,len(arr))
