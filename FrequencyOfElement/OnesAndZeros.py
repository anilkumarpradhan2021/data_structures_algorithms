'''
Created on 27-Jun-2016

@author: anpradha
'''


def Ones_Zeros():
    a = [1, 1, 1, 1, 0, 0, 0, 0, 0]
    #a = [0, 0, 0, 0, 0]
    low = 0;
    high = len(a) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        
        if mid == 0 and a[mid] == 0:
            print("start")
            print(mid)
            break;
            
        if a[mid] == 0:
            if a[mid - 1] > 0:
                print("start")
                print(mid)
                break;
            else:
                high = mid - 1 ;
        else:
            low = mid + 1    
     
if __name__ == '__main__':
    Ones_Zeros()
