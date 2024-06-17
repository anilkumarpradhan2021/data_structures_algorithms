'''
Created on 21-Nov-2019

@author: anpradha

Cutting a Rod | DP-13
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
For example, if length of the rod is 8 and the values of different pieces are given as following, 
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20


'''


# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price, n): 
    val = [0 for x in range(n + 1)] 
  
    ''' Build the table val[] in bottom up manner and return the last entry from the table '''
    for i in range(0, n + 1): 
        for j in range(i):  
            print("i = ", i , "j = " ,j)
            print(val)
            val[i] = max(val[i], price[j] + val[i - 1 - j]) 
            print(val)
  
    return val[n] 
  


if __name__ == '__main__':
    # Driver program to test above functions 
    # arr = [1, 5, 8, 9, 10, 17, 17, 20] 
    arr = [1, 5, 8, 9] 
    
    size = len(arr) 
    print("Maximum Obtainable Value is " + str(cutRod(arr, size))) 
