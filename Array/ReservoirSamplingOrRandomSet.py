'''
Created on 19-Nov-2019

@author: anpradha

Reservoir Sampling
Reservoir sampling is a family of randomized algorithms for randomly choosing k samples from a list of n items, where n is either a very large or unknown number. Typically n is large enough that the list doesn’t fit into main memory. For example, a list of search queries in Google and Facebook.

So we are given a big array (or stream) of numbers (to simplify), and we need to write an efficient function to randomly select k numbers where 1 <= k <= n. Let the input array be stream[].



It can be solved in O(n) time. The solution also suits well for input in the form of stream. The idea is similar to this post. Following are the steps.

1) Create an array reservoir[0..k-1] and copy first k items of stream[] to it.
2) Now one by one consider all items from (k+1)th item to nth item.
…a) Generate a random number from 0 to i where i is index of current item in stream[]. Let the generated random number is j.
…b) If j is in range 0 to k-1, replace reservoir[j] with arr[i]


'''
import random


def selectKRandomItems(stream, k):
    ''' create a array with k element '''
    aux = stream[:k]
    
    
    for i in range(k, len(stream)):
        ''' find a random index between 0 to i , if random index < k , then swap'''
        randomIndex = random.randint(0, i)
        if randomIndex < k:
            aux[randomIndex], stream[i] = stream[i], aux[randomIndex]
    
    print(aux)    

if __name__ == '__main__':
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    k = 5
    selectKRandomItems(stream, k)
    
