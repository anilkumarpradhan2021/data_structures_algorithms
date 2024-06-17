'''
Created on 09-Oct-2019

@author: anpradha
Living People: Given a list of people with their birth and death years, implement a method to
compute the year with the most number of people alive. You may assume that all people were born
between 1900 and 2000 (inclusive). If a index was alive during any portion of that year, they should
be included in that year's count. For example, index (birth= 1908, death= 1909) is included in the
counts for both 1908 and 1909.

birth: 12 20 10 01 10 23 13 90 83 75
death: 15 90 98 72 98 82 98 98 99 94

This algorithm takesO(R + P) time, where R is the range of years and Pis the number of people


'''

if __name__ == '__main__':
    birth = [1912, 1920, 1910, 1901, 1910, 1923, 1913, 1990, 1983, 1975]
    death = [1915, 1990, 1998, 1972, 1998, 1982, 1998, 1998, 1999, 1994]
    
    # for creating a aux arrry , i am removing 1900 for each
    
    birth = [i - 1900 for i in birth]
    death = [i - 1900 for i in death]

    
    print(birth)
    print(death)
    
    aux_array_size = max(max(birth) , max(death))
    aux_array = [0] * (aux_array_size + 2)
    
    max_alive = float("-inf")
    for index in range(len(birth)):
       
        # for birth
        aux_array[birth[index]] = aux_array[birth[index]] + 1
                
        # for death (This + one is required because for the same year the index cloud be born and dead also , but it should be considered alive for that year)
        aux_array[death[index] + 1 ] = aux_array[death[index] + 1] - 1
    
    
    current_sum = 0
    for year in aux_array:
        current_sum = max(current_sum, current_sum + year)
        print(current_sum,year)
        max_alive = max(max_alive, current_sum)
    
    print(aux_array)
    print("max_alive : " , max_alive)    

