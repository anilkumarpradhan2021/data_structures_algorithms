'''
Created on 09-Sep-2016

@author: anpradha
Stock Buy Sell to Maximize Profit
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
For example, 
if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3. 
Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.


Following is algorithm for this problem.
1. Find the local minima and store it as starting index. If not exists, return.
2. Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
3. Update the solution (Increment count of buy sell pairs)
4. Repeat the above steps if end is not reached.

Complexity :  O(n)

'''

class Stock():
    def __init__(self, buy, sell):
        self.buy = buy
        self.sell = sell    
    
    def __repr__(self):
        return "Buying Price : " + str(self.buy) + " , Selling Price : " + str(self.sell)
    
    
if __name__ == '__main__':
    arr = [100, 180, 260, 310, 40, 535, 695]
    
    ''' create stock temp variable'''
    stock_temp = []
    i = 0
    
    ''' Prices must be given for at least two days '''
    if len(arr) <= 1:
        print("Solution is not possible")
        
    while i < len(arr):
        print("outer : " + str(i))
        ''' find the local minimum '''
        while i < len(arr) - 1 and arr[i + 1] < arr[i]:
            i = i + 1
        
        '''Store the index of minima'''
        buy = i
                
        ''' find the local maximum'''
        while i < len(arr) - 1 and arr[i + 1] > arr[i]:
            i = i + 1
        
        ''' Store the index of maxima '''
        sell = i
        stock_temp.append(Stock(buy, sell))

        ''' If we reached the end, break as no further solution possible '''
        if i == len(arr) - 1:
            break
    
    print(stock_temp)        
    

        
    

