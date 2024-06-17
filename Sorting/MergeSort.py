'''
Created on 08-Sep-2016

@author: anpradha
'''


'''

If length of array > l
     1. Find the middle point to divide the array into two halves:  
             middle = Length of array /2
     2. Call mergeSort for first half:   
     3. Call mergeSort for second half:
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(left,right)
'''
def merge_sort(x):
    if len(x) < 2:
        print("x: " +str(x))
        return x
        
    else:
        mid = len(x) // 2
        left = merge_sort(x[:mid])
        right = merge_sort(x[mid:])
        return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                left.pop(0)
    while len(right) > 0:
        result.append(right.pop(0))
        
    while len(left) > 0:
        result.append(left.pop(0))
    print(result)    
    return result

if __name__ == '__main__':
    arr = [12, 23, 1, 24, 111, 34, 12, 2 ]
    print("Array Before Sort : " + str(arr))
    arr = merge_sort(arr)
    print("Array after Sort : " + str(arr))
