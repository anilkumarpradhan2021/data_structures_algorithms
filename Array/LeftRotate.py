'''
Created on 06-May-2017

@author: anpradha


Python Program for array rotation

Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

Time complexity : O(n * d)
Auxiliary Space : O(1)

'''


def leftRotateArray(arr, n):
    for i in range(n):
        for i in range(len(arr) - 1):
            arr[i] , arr[i + 1] = arr[i + 1] , arr[i]
    
    print(arr)    


'''

Time complexity : O(n)
Auxiliary Space : O(1)


'''

def leftRotate(arr, n, k): 
      
    # Print array  
    # after k rotations 
    for i in range(k, k + n): 
        print(str(arr[i % n]),
                   end=" ") 

    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    leftRotateArray(arr, 2)

    arr = [1, 2, 3, 4, 5]
    leftRotate(arr, len(arr), 2)
