'''
Created on 20-Sep-2016

@author: anpradha


Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of 
this subset is smaller than or equal to W.

You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.

Please watch the download video for easy understanding

https://www.youtube.com/watch?v=8LusJS5-AGo

formula : 

                0    if i = 0 or w = 0
    c[i,w]  =    c[i-1, w]    if wi ≥ 0 
                 max [vi + c[i-1, w-wi], c[i-1, w]}    if i>0 and w ≥  wi
                 
                 
This says that the value of the solution to i items either include ith item, 
in which case it is vi plus a subproblem solution for (i - 1) items and the weight excluding wi, or does not include ith item, 
in which case it is a subproblem's solution for (i - 1) items and the same weight. That is, if the thief picks item i,
 thief takes vi value, and thief can choose from items w - wi, and get c[i - 1, w - wi] additional value. On other hand, 
 if thief decides not to take item i, thief can choose from item 1,2, . . . , i- 1 upto the weight limit w, and get c[i - 1, w] value.
  The better of these two choices should be made.                 
'''

def kanpSack(value, weight, maximum_weight):
    ''' build the 2 dimensional  array , number of column are the maximum allowed weight +1 , and row is same as that of size of weight/value array ''' 
    k = [[0 for x in range(maximum_weight + 1)] for  x in range(len(weight) + 1)]
    
    
    ''' i represent value , j represent weight '''
    for i in range(len(value) + 1):
        for j in range(maximum_weight + 1):
            ''' 1st column all values are zero  as weight is 0'''
            if i == 0 or j == 0:
                k[i][j] = 0
            # check if current item[weight] is < current weight     
            elif weight[i - 1] <= j:
                    k[i][j] = max((value[i - 1] + k[i - 1][j - weight[i - 1]]), k[i - 1][j]) 
            else:
                k[i][j] = k[i - 1][j]    
    
    print('matrix : ')
    for i in range(len(k)):
        for j in range(len(k[i])):
            print(k[i][j],end=' ')
        print()
        
            
    print("Maximum Value can be accommodate : " + str(k[i][j]))
    
'''
    This one has only one dimentional array for temp
'''    
def kanpSack2(value, weight, maximum_weight):
    
    # Making the dp array
    dp = [0 for i in range(maximum_weight+1)]

    # Taking first i elements
    for i in range(len(value)):
      
        # Starting from back,
        # so that we also have data of
        # previous computation when taking i items
        for j in range(maximum_weight, 0, -1):
            if weight[i] <= j:
                
                # Finding the maximum value
                dp[j] = max(dp[j], value[i] + dp[j-weight[i]])
            print(dp)    
    
    print(dp)
    # Returning the maximum value of knapsack
    return dp[maximum_weight]
                
                    
if __name__ == '__main__':
    value = [1, 4, 5, 7]
    weight = [1, 3, 4, 5]
    maximum_weight = 7
    #value = [60, 100, 120]
    #weight = [10, 20, 30]
    #maximum_weight = 50
    
    kanpSack(value, weight, maximum_weight)
    kanpSack2(value, weight, maximum_weight)
    
