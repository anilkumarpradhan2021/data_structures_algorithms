'''
Created on 03-Oct-2016

@author: anpradha
'''

if __name__ == '__main__':
    s = {1, 2, 2, 2, 2, 2}
    print("s : " + str(s))
    
    s1 = {5}
    s1.add(1)
    s1.add(1)
    s1.add(1)
    
    print("s1 : " + str(s1))
    
    s2 = set()
    s2.add(1)
    s2.add(2)
    s2.add(2)
    s2.add(3)
    
    
    print("s2 : " + str(s2))
    
    list = [1, 2, 1, 1, 13, 4, 4]
    s3 = set(list)
    print("s3 : " + str(s3))
    
    
    
    
    
