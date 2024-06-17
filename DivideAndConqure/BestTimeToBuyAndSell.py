'''
Created on 24-Sep-2016

@author: anpradha


Problem -1 :
Maximum difference between two elements such that larger element appears after the smaller number

Given an array arr[] of integers, find out the difference between any two elements such that larger element appears after the
 smaller number in arr[].

Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2). 
If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)

Problem -2 
Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to buy one share of the stock and sell one share of the stock, design an algorithm 
to find the best times to buy and sell.

Time Complexity: O(n)
Auxiliary Space: O(1)

To solve this problem efficiently, you would need to track the minimum value’s index. As you traverse, update the minimum value’s 
index when a new minimum is met. Then, compare the difference of the current element with the minimum value. Save the buy and sell 
time when the difference exceeds our maximum difference (also update the maximum difference).
 
 
KEY POINT IS KEEP TRACK OF MINIMUM NUMBER/STOCK PRICE 

'''

if __name__ == '__main__':
    stock_price = [7, 9, 5, 16, 3, 2 ]
    print(stock_price)
    minimum_stock_price = stock_price[0]
    maximum_difference_in_stock = 0
    minimum_stock_price_index = 0
    sell_index = 0
    buy_index = 0
    for i in range(1, len(stock_price)):
        if stock_price[i] < minimum_stock_price :
            minimum_stock_price = stock_price[i]
            minimum_stock_price_index = i  #update the minimum value 
        if stock_price[i] - minimum_stock_price > maximum_difference_in_stock:
            maximum_difference_in_stock = stock_price[i] - minimum_stock_price
            sell_index = i
            buy_index = minimum_stock_price_index
    
    print("maximum_difference_in_stock : " + str(maximum_difference_in_stock))         
    print("sell_index : " + str(sell_index))          
    print("buy_index : " + str(buy_index))          


            