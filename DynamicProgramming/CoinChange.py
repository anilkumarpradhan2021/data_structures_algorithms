'''
Created on 21-Sep-2016

@author: anpradha

Given coins of certain denominations with infinite supply find minimum number of coins it takes to form given total

The change-making problem addresses the following question: how can a given amount of money be made with the least number of coins of given denominations? 
It is a knapsack type problem, and has applications wider than just currency.

its a Bottom up DP

Downloaded a Video , please watch it for better understanding
https://www.youtube.com/watch?v=Y0ZqKpToTic
'''

''' This is for minimum coin required '''


def coin_change(coins, total):
    '''  We need n+1 rows as the table is constructed in bottom up manner using the base case 0 value case (n = 0) '''
    T = [0 if x == 0 else float('inf') for x in range(0, total + 1)]
    print(T)
    R = [-1 for _ in range(total + 1)]
    
    for i in range(len(coins)):
        for j in range(1, len(T)):
            if coins[i] <= j:
                '''Formula is T[j] = Min(T[j],(1+T[j-coin[i]]))'''
                if T[j] > (1 + T[j - coins[i]]):
                    T[j] = 1 + T[j - coins[i]]
                    R[j] = i
    
    print("T" , T)
    print(R)
    print("Minimum coin required : " , T[-1])
    print_coins(coins, R)

''' 
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
 So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.



This is for maximum  possible coin required 

'''


def max_coin_change(coins, total):
    '''  We need n+1 rows as the table is constructed in bottom up manner using the base case 0 value case (n = 0) '''
    T = [0 if x == 0 else float('-inf') for x in range(0, total + 1)]
    # T[0] = 1
    print(T)
    print("Coins :" ,coins)
    print("Total : ", total)
    
    for j in range(len(coins)):
        for i in range(total + 1):
            if coins[j] <= i:
                    T[i] = max(T[i], 1 + T[i - coins[j]])
            print(T)
    print("Maximum coin required : " , T[-1])


def print_coins(coins, R):
    start = len(R) - 1
    if start == -1:
        print("No solution possible")
        return
    
    temp_coins = []
    while(start > 0):
        coin = coins[R[start]]
        temp_coins.append(coin)
        start = start - coin
    print(temp_coins)   


if __name__ == '__main__':
    coins = [1, 5, 6, 8] 
    total = 11 
    coins = [2, 5, 3, 6]
    total = 3
    #coin_change(coins, total)
    max_coin_change(coins, total)
    
