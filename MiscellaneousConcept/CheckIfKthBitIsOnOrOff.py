'''
Created on 12-Oct-2016

@author: anpradha
'''


'''
It will check for kth bit , if kth bit is 1 return 1 else return 0
'''

def checkIfKthBitIsOnOrOff(n, k):
    if n & (1 << (k - 1)):
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(checkIfKthBitIsOnOrOff(4,1))
    print(checkIfKthBitIsOnOrOff(4,2))
    print(checkIfKthBitIsOnOrOff(4,3))