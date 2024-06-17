'''
Created on 09-Sep-2016

@author: anpradha
'''
def bucket_sort(arr):
    
    '''
    This logic works only for decimal number ,it wont work for integer .
    Idea is 
    let arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434,0.3434]
    let crate an aux array like aux = [0,0,0,0,0,0,0]
    Let our hash function is arr[i] * 10 (for simplicity)
    so hash for all array element wound look like 
    arr = [8.97, 5.65, 6.56, 1.234, 6.65, 3.434,3.434]
    further more we can make them to whole number 
    arr = [8, 5, 6, 1, 6, 3,3]
    aux_index = [0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
    aux =       [0, 1 , 0 , 2 , 0 , 1 , 2 , 0 , 1]
    then same concept like count sort is applied here
      
    
      
    Create n buckets  , here i have created a array of array  
    
    buckets = [[],[],[]]
    bucket = [bucket1[value1,value2...],
                                    bucket2[value1,value2...]...]
    ....
    
    
    '''
    
    '''
    Create number buckets are equals to "size"
    '''
     
    size = len(arr)
    print("size : " + str(size))
    buckets = [[] for i in range(size)]
    
    # put arr in bucket        
    for i in range(len(arr)):
        num = size * arr[i]
        print("Num  : " + str(num))
        buckets[int(num)].append(arr[i])
    print(buckets)  
    
    '''
    Sort individual buckets
    '''
    
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])  
        
    print(buckets)  
    
    index = 0 
    for i in range(len(buckets)):
        while len(buckets[i]) > 0:
            arr[index] = buckets[i].pop(0)
            index = index + 1
            

if __name__ == '__main__':
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Array Before Sort : " + str(arr))
    bucket_sort(arr)
    print("Array After bubble Sort : " + str(arr))
