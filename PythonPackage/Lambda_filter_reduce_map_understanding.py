'''
Created on 02-Sep-2016

@author: anpradha


http://www.python-course.eu/lambda.php

'''
from functools import reduce


if __name__ == '__main__':
    '''
    lambda argument_list: expression 
    
    '''
    f = lambda x, y : x + y
    print(f(1, 2))

    '''
    r = map(func, seq)

    '''

    def fahrenheit(T):
        return ((float(9) / 5) * T + 32)
    
    def celsius(T):
        return (float(5) / 9) * (T - 32)
    
    temp = [36.5, 37, 37.5, 39]
    
    F = list(map(fahrenheit, temp))
    print("F  : " + str(F))
    C = list(map(celsius, temp))
    print("C  : " + str(C))
    
    # With lambda function
    F1 = list(map(lambda f : ((float(9) / 5) * f + 32), temp))
    print("F1  : " + str(F1))
    
    '''map() can be applied to more than one list. The lists have to have the same length. 
    map() will apply its lambda function to the elements of the argument lists, i.e. 
    it first applies to the elements with the 0th index, then to the elements with the 1st index until the n-th index is reached'''
    
    a = [1, 2, 3, 4]
    b = [17, 12, 11, 10]
    c = [-1, -4, 5, 9]
    
    sum_of_lists = list(map(lambda x, y, z:x + y + z, a, b, c))
    print("sum_of_lists : " + str(sum_of_lists))
    
    '''
    Filter: 
    Syntax:
    filter(function, list)
    '''
    
    odd_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = list(filter(lambda x:x % 2 == 0 , odd_even))
    print("Only even numbers after filter : " + str(even))

    odd = list(filter(lambda x:x % 2 != 0 , odd_even))
    print("Only Odd numbers after filter : " + str(odd))
    
    '''
    Reducing a list :
    
    Syntax:
    reduce(func, seq)
    
    reduce is functools in 3.2  so need to import 
    
    from functools import reduce
    
    '''
    #  sum of numbers from 1 to 100
    sum = reduce(lambda x, y : x + y, range(1, 101))
    print("Sum is : " + str(sum))
    
    max_list = [13, 41, 2, 4, 5]
    find_max = reduce(lambda x, y: x if (x > y) else y, max_list)
    print("maximum : " + str(find_max))
    
    
    ''' max function with lambda '''
    arr_find_max = [1, 2, 24, 56, 55, 66]
    int_max = max(arr_find_max)
    print("Int_Max  from a list : " + str(int_max))
    

    arr_find_max2 = [1, 2, 24, 56, 55, 66]
    int_max2 = max(arr_find_max2,key=lambda x : x )
    print("Int_Max2  from a list : " + str(int_max2))
    
    
    dict_find_maximum = {"name1":10, "name2":2, "name3":10, "name4":222, "name5":102, "name6":21}
    print(dict_find_maximum)
    int_max = max(dict_find_maximum)
    print("Int_Max  from a Dictionary : " + str(int_max))
    
    # Modify the logic for max
    int_max = max(dict_find_maximum, key=lambda x:dict_find_maximum[x])
    print("Int_Max  from a Dictionary depending on value : " + str(int_max))
    
    

    
