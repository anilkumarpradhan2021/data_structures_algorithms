'''
Prefix Sum ArrayGiven an array arr[] of size N, the task is to compute and return its prefix sum array. 

Prefix Sum is a precomputation technique in which the sum of all the elements of the original array from an 0th index to ith index

Therefore, this suffix sum array will be created using the relation: 

Prefix[i] = arr[0] + arr[1] +....+ arr[i]      

The original list : [3, 4, 1, 7, 9, 1]
The prefix sum list is : [3, 7, 8, 15, 24, 25]
Time Complexity: O(n)
Auxiliary Space: O(n)

'''

def prefix_sum(arr):
    arr_length = len(arr)
    prefix_sum_arr = [0]*arr_length
    prefix_sum_arr[0] = arr[0]
    for i in range(1,arr_length):
        prefix_sum_arr[i] = prefix_sum_arr[i-1] + arr[i]
    print("Before")
    print(arr)
    print("After")
    print(prefix_sum_arr)
if __name__ == '__main__':
    arr = [15, 10, 25, 5, 10, 20]
    prefix_sum(arr)