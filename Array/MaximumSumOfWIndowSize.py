'''
Created on 17-Jul-2019

@author: anpradha
'''

if __name__ == '__main__':
    k = 4
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
    window_sum = sum(arr[:k])
    max_sum = 0
    k = 4
    for i in range(k,len(arr)):
        window_sum = window_sum + arr[i] - arr[i-k]
        max_sum = max(max_sum,window_sum)
    print(max_sum)    