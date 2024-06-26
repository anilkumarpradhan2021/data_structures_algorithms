'''
Created on 16-Nov-2019

@author: anpradha


Cutting a Rod | DP-13

Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.
For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20



'''
# A Dynamic Programming solution for Rod cutting problem 
INT_MIN = -32767

  
# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price, n): 
    val = [0 for x in range(n + 1)] 
    val[0] = 0
  
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for i in range(1, n + 1): 
        max_val = INT_MIN 
        for j in range(0,i): 
            max_val = max(max_val, price[j] + val[i - j - 1]) 
            #print(i ,j , max_val)
        val[i] = max_val 
        #print(val)

    print(val)
    return val[n] 

def cutRod2(price, n): 
    val = [0 for x in range(n + 1)] 
  
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for i in range(1, n + 1): 
        for j in range(0,i): 
            val[i] = max(val[i], price[j] + val[i - j - 1]) 

    print(val)
    return val[n] 

if __name__ == '__main__':
    arr = [1, 5, 8, 9, 10, 17, 17, 20] 
    size = len(arr) 
    print("Maximum Obtainable Value is", cutRod(arr, size)) 
    print("Maximum Obtainable Value is", cutRod2(arr, size)) 
