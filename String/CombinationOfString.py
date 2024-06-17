'''
Created on 03-Sep-2016

@author: anpradha
'''

'''
    arr = complete array [input]
    temp_arr = temp arry to store the result and print when the lenth is same as r
    start_index and end_index  ---> Staring and Ending indexes in arr[] 
    index  ---> Current index in temp_data[]
    number_of_char ---> Size of a combination to be printed
'''


def combinationUtil(arr, temp_arr, start_index, end_index, index, number_of_char):
    
    # Current combination is ready to be printed, print it
    if index == number_of_char:
        print(temp_arr)
        return
    
    i = start_index
    while start_index <= end_index and end_index - i + 1 >= number_of_char - index:
        temp_arr[index] = arr[i]
        combinationUtil(arr, temp_arr, i + 1, end_index, index + 1, number_of_char)
        i = i + 1


'''
    arr = complete array [input]
    temp_arr = temp arry to store the result and print when the lenth is same as r
    start_index and end_index  ---> Staring and Ending indexes in arr[] 
    index  ---> Current index in temp_data[]
    number_of_char ---> Size of a combination to be printed
'''


def combinationUtil2(arr, temp_arr, start_index, end_index, temp_index, number_of_char):
    
    ''' below code is required only when we have duplicate in arr and precondition is array is sorted '''
    while start_index < end_index - 1 and arr[start_index] == arr[start_index + 1]:
        start_index = start_index + 1
        
    # Current combination is ready to be printed, print it
    if temp_index == number_of_char:
        print(temp_arr)
        return
    
    '''When no more elements are there to put in temp_data[] '''
    if start_index < end_index:
    
        '''current is included, put next at next location '''
        temp_arr[temp_index] = arr[start_index]
        combinationUtil2(arr, temp_arr, start_index + 1, end_index, temp_index + 1, number_of_char)
        
        '''current is excluded, replace it with next (Note that start_index is increased , but index is not changed)'''
        combinationUtil2(arr, temp_arr, start_index + 1, end_index, temp_index, number_of_char)
                



if __name__ == '__main__':
    arr = list("12345")
    # arr = list("121")

    ''' below code is required only when we have duplicate in arr so sorting '''
    arr = sorted(arr)

    arr_length = len(arr)
    r = 3
    # A temporary array to store all combination one by one , so create with same length as r
    temp_arr = [0 for x in range(r)]
    # combinationUtil(arr, temp_arr, 0, arr_length - 1, 0, r)
    combinationUtil2(arr, temp_arr, 0, arr_length, 0, r)
    
    
