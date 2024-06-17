'''
Created on 03-Nov-2019

@author: anpradha
'''


def printPermutationOfArray(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        start_index = arr[i]
        rest_of_element = arr[:i] + arr[i + 1:]
        for j in printPermutationOfArray(rest_of_element):
            result.append([start_index] + j)
    return result        
            

def nextperm(a):
    n = len(a)
    i = n - 1
    while i > 0 and a[i - 1] > a[i]:
        i = i - 1
    j = i
    k = n - 1
    while j < k:
        a[j], a[k] = a[k], a[j]
        j = j + 1
        k = k - 1
    if i == 0:
        return False
    else:
        j = i
        while a[j] < a[i - 1]:
            j = j + 1
        a[i - 1], a[j] = a[j], a[i - 1]
        return True

 
def perm3(n):
    # sort the array
    sorted(n)
    
    u = [tuple(n)]
    while nextperm(n):
        u.append(tuple(n))
    return u


'''
Heap's algorithm

The algorithm generates (n-1)! permutations of the first n-1 elements, adjoining the last element to each of these. This will generate all of the permutations that end with the last element.
If n is odd, 
    swap the first and last element 
and 
if n is even, 
    then swap the ith element (i is the counter starting from 0) and the last element 

and repeat the above algorithm till i is less than n.

In each iteration, the algorithm will produce all the permutations that end with the current last element.
'''


def heapPermutation(a, size): 
      
    # if size becomes 1 then prints the obtained 
    # permutation 
    if (size == 1): 
        print(a) 
        return
  
    for i in range(size): 
        heapPermutation(a, size - 1); 
  
        # if size is odd, swap first and last 
        # element 
        # else If size is even, swap ith and last element 
        if size & 1: 
            a[0], a[size - 1] = a[size - 1], a[0] 
        else: 
            a[i], a[size - 1] = a[size - 1], a[i] 


def heapPermutationIterative(a, n): 
    indexs = [0 for i in range(len(a))]
    i = 0
    while i < len(a):
        #print("indexs " , indexs , "i " , i)

        if indexs[i] < i:
            if i % 2 == 0:
                a[0], a[n - 1] = a[n - 1], a[0]
            else:
                a[i], a[n - 1] = a[n - 1], a[i]
            print(a)
            indexs[i] = indexs[i] + 1 
            i = 0
        else:
            indexs[i] = 0
            i = i + 1

    #print("indexs " , indexs)


if __name__ == '__main__':
    arr = [1, 2, 3]
    #arr = ["A","B", "C"]
    # print(perm3(arr))
    heapPermutation(arr, len(arr))
    #heapPermutationIterative(arr, len(arr))
        
    
