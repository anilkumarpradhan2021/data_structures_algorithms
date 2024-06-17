'''
Created on 04-Jan-2024

@author: anpradha
'''



'''
Given a sorted array , find the index where we can insert an array and still the array will be sorted 
e.g
arr = [10,20,30,40]
if 5 , we can insert at 0th position and still it wll be sorted like 5,10,20,30,40
if 45 we can insert at 4th position  and still it wll be sorted like 10,20,30,40,45
if 35 we can insert at 3rd position  and still it wll be sorted like 10,20,30,35,40

'''

arr = [10,20,30,40]
low = 0
high = len(arr) -1
n = 35
position_to_insert = 0
while low <=high:
    mid = (low + high) // 2
    if arr[mid] > n:
        high = mid -1
    else:
        low = mid +1
        position_to_insert = mid +1 
print(position_to_insert)        
        
            