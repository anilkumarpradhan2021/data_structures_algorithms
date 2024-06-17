'''
Created on 24-Sep-2019

@author: anpradha

Set the bit means 
N= 7 
k=0
Bin(7) = 111 
O/p : 7


N= 8
k= 0
Bin(8) = 1000 
O/p : 1001 = > 9

N= 8
k= 1
Bin(8) = 1000 
O/p : 1010 = > 10

 
'''


def setBit(number, k):
    return (number | 1 << k)


if __name__ == '__main__':
    print(setBit(8, 0))
    print(setBit(8, 1))
