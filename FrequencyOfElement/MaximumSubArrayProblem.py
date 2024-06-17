'''
Created on 22-Jul-2016

@author: anpradha
'''

def max_subarray(array):
    maximum_sum = 0;
    start_index = 0
    end_index = 0 
    current_sum = 0;
    for i in range(len(array)):
        current_sum = max(0, current_sum + array[i])
        if current_sum == 0:
            start_index = i
        if  current_sum > maximum_sum:
            end_index = i
        maximum_sum = max(current_sum, maximum_sum)
        
    print("Maximum Sum : " + str(maximum_sum))    
    print("start index : " + str(start_index))
    print("end index : " + str(end_index))


def max_subarray_with_all_negative(array):
    maximum_sum = array[0];
    start_index = 0
    end_index = 0 
    current_sum = array[0];
    for i in range(len(array)):
        current_sum = max(array[i], current_sum + array[i])
        if  current_sum > maximum_sum:
            end_index = i
            start_index = i
        maximum_sum = max(current_sum, maximum_sum)
        
    print("Maximum Sum : " + str(maximum_sum))    
    print("start index : " + str(start_index))
    print("end index : " + str(end_index))
    
if __name__ == '__main__':
    array = [3, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    max_subarray(array)
    array = [-31, -25, -16, -23, -7, -5, -22, -4]
    max_subarray_with_all_negative(array)
    
