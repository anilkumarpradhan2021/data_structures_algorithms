'''
Created on 02-Sep-2016

@author: anpradha
'''

if __name__ == '__main__':
    pass
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    print("arr : " + str(arr))
    print("arr[::] : " + str(arr[::]))  # Start from 0  and print all till end 
    print("arr[:4] " + str(arr[:4]))  # Start from 0  and print all till 4th element
    print("arr[2:] : " + str(arr[2:]))  # Start from 2  and print all till end
    print("arr[::-1] : " + str(arr[::-1]))  # reverse print 
    print("arr[1:4] : " + str(arr[1:4]))  # Print between 1 and 4 index
    print("arr[0:-1] : " + str(arr[0:-1]))  # Start from 0 and exclude last one
    print("arr[0:-2] : " + str(arr[0:-2]))  # Start from 0 and exclude last two
    print("arr[0::2] : " + str(arr[0::2]))  # Start from 0 and print each 2nd element
    print("arr[::4] : " + str(arr[::4]))  # Start from 0 and print each 4th element
    print("arr[::-1] : " + str(arr[::-1]))  # Start from end and print each element from end (reverse)
    print("arr[::-2] : " + str(arr[::-2]))  # Start from end and print each 2nd element from end
    test = arr[1:-2] # It returns a list 
    print(test)
               
    

    
