'''
Created on 10-Aug-2016

@author: anpradha
'''

if __name__ == '__main__':
    pass
    a = [-1, 0, 1, 6, 6, 0, 0, 2, 7]
    print(a)
    reference_hash = {}
    max_depth = 0
    for i in range(0, len(a)):
        current_depth = 0;
        j = i
        while (a[j] != -1):
            j = a[j]
            if j in reference_hash :
                current_depth = current_depth + reference_hash[j] + 1
                break
            else:
                current_depth = current_depth + 1    
        
        if current_depth > max_depth :
            max_depth = current_depth
        reference_hash[i] = current_depth   
    
    print(max_depth)  
    print(reference_hash)      
