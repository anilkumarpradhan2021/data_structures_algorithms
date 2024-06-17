'''
Created on 17-Jan-2020

@author: anpradha

Print all pairs with given sum
Given an array of integers, and a number ‘sum’, print all pairs in the array whose sum is equal to ‘sum’.

Examples :
Input  :  arr[] = {1, 5, 7, -1, 5}, 
          sum = 6
Output : (1, 5) (7, -1) (1, 5)

Input  :  arr[] = {2, 5, 17, -1}, 
          sum = 7
Output :  (2, 5)

Method 2 (Use hashing).
We create an empty hash table. Now we traverse through the array and check for pairs in hash table. If a matching element is found, we print the pair number of times equal to number of occurrences of the matching element.

Note that the worst case of time complexity of this solution is O(c + n) where c is count of pairs with given sum.


'''


def findAllPairsWIthSum(arr, sum):
    d = {}
    for i in arr:
        ''' 
        Logic is sum - i should be in d and this pair is not printed , 
        so to track we are using False/True Flag , 
        Flase means not printed, Once printed , make it True
        '''
        if sum- i in d and d.get(i,False) is False:
            print("Sum found {sum} : ".format(sum=sum) , i, sum - i)
            d[i] = True
        d[i] = d.get(i,False)   
        #print(d)

    
if __name__ == '__main__':
    arr = 1, 5, 7, -1, 5    
    arr = [1, 5, 7, -1, 5, 3, 3, 3]
    sum = 6
    findAllPairsWIthSum(arr,sum)
