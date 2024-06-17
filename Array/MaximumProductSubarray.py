'''
Created on 29-Jul-2019

@author: anpradha
'''

'''

Given an array A[] that contains both positive and negative integers, find the maximum product subarray.


Examples :

Input: A[] = { 6, -3, -10, 0, 2 }
Output: 180  // The subarray is {6, -3, -10}

Input: A[] = {-1, -3, -10, 0, 60 }
Output: 60  // The subarray is {60}

Input: A[] = { -2, -3, 0, -2, -40 }
Output: 80  // The subarray is {-2, -40}



'''


def maxSubArrayProduct(arr):
    max_product = arr[0]
    max_product_till_now = arr[0]
    min_product_till_now = arr[0]
    
    for i in range(1, len(arr)):
        
        '''
         When multiplied by -ve  number, maxVal becomes  minVal and minVal  becomes maxVal.
        '''    
        if arr[i] < 0:
            max_product_till_now , min_product_till_now = min_product_till_now, max_product_till_now
    
        '''
            max_product_till_now and min_product_till_now stores  the product of subarray ending at arr[i].
        '''
        max_product_till_now = max(arr[i], max_product_till_now * arr[i])
        
        min_product_till_now = min(arr[i], min_product_till_now * arr[i])
        
        # Max Product of array.
        max_product = max(max_product, max_product_till_now)
        
    print(max_product)    
   

if __name__ == '__main__':
    arr = [  6, -3, -10, 0, 2 ]
    maxSubArrayProduct(arr)
        
