'''
Created on 03-Jun-2019

@author: anpradha
'''

'''
    Vectors are strictly 1-d arrays and matrices are 2-d

'''

import numpy as np

if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    print("Python My_list : " , my_list) # Python My_list :  [1, 2, 3, 4]
    print("Python List Type: " , type(my_list), end="\n\n") # Python List Type:  <class 'list'>

    np_vector = np.array(my_list)
    print("Vector : " , np_vector) # Vector :  [1 2 3 4]
    print("Vector Type: " , type(np_vector), end="\n\n") # Vector Type:  <class 'numpy.ndarray'>
     
    my_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("my_matrix : ") 
    print(my_matrix)
    print("my_matrix Type: " , type(my_matrix), end="\n\n")
    
    # # Built-in Methods
    '''
    arange
        arange([start,] stop[, step,], dtype=None)

        Return evenly spaced values within a given interval.

    '''
    print("Range Between 1 to 10              : " , np.arange(1, 10))
    print("Range Between 1 to 10 with step 2  : " , np.arange(1, 10, 2), end="\n\n")

    '''
        ### zeros and ones

        Generate arrays of zeros or ones
    '''
    print("Create Array of Zeros 1D          : " , np.zeros(3))
    print("Create Array of Zeros 2D          : " , np.zeros((3,3)))
