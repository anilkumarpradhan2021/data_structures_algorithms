'''
Suffix Sum is a precomputation technique in which the sum of all the elements of the original array from an index i till the end of the array is computed.


Input: arr[] = { 15, 10, 25, 5, 10, 20 } , N = 6
Output: suffixSum[] = { 85, 70, 60, 35, 30, 20}

https://www.geeksforgeeks.org/suffix-sum-array/


'''
def suffix_sum(arr):
    arr_length = len(arr)
    suffix_sum_arr = [0]*arr_length
    suffix_sum_arr[arr_length-1] = arr[arr_length-1]
    
    for i in range(arr_length-2,-1,-1):
        suffix_sum_arr[i] = suffix_sum_arr[i+1] + arr[i]
    print("Before")
    print(arr)
    print("After")
    print(suffix_sum_arr)
if __name__ == '__main__':
    arr = [15, 10, 25, 5, 10, 20]
    suffix_sum(arr)