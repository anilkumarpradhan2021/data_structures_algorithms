'''
Created on 29-Oct-2019

@author: anpradha

Shortest Supersequence: You are given two arrays, one shorter (with all distinct elements) and one
longer. Find the shortest subarray in the longer array that contains all the elements in the shorter
array. The items can appear in any order.
EXAMPLE
Input:
{1, 5, 9}
{7, 5, 9, 0, 2, 1, 3, 5. 7, 9. 1, 1, 5, 8, 8, 9, 7}
                     -----------
Output:[7, 10] (the underlined portion above)


For any Doubt: Please refer Cracking the Coding Interview, 6th Edition page num:  588
dont worry about other solution

Complexity :  O(SB)
S = length of small array
B = Length of big array

'''

if __name__ == '__main__':
    bigArray = [7, 5, 9, 9, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    smallArray = [1, 5, 9]
    
    d = {}
    
    ''' find out all the occurrence of small array element in big array'''
    for j in range(len(smallArray)):
        for i in range(len(bigArray)):
            if bigArray[i] == smallArray[j]:
                d[smallArray[j]] = d.get(smallArray[j], []) + [i]
        
    print("all occurrence of small array in big array " , d)
    
    ''' find the minimum '''
    bestStart = 0
    bestEnd = float("inf")

    while True:    
        tempArray = []
        for key in d.keys():
            if len(d[key]) > 0:
                tempArray.append((key , d[key][0]))
        
        ''' break when any of the element don't have any occurrence further'''
        if len(tempArray) < len(d):
            break
        
        ''' find the minimum starting index and remove that index from d'''
        currentStart = min(tempArray, key=lambda x:x[1]) 
        
        '''delete the value from d''' 
        d[currentStart[0]].remove(currentStart[1])
        
        currentStart = currentStart[1]

        ''' find the maximum index , which we need to accommodate all elements in small array'''        
        currentEnd = max(tempArray, key=lambda x:x[1])[1]    
        
        ''' update when we get the shorter range'''
        if (bestEnd - bestStart) > (currentEnd - currentStart):
            bestEnd = currentEnd
            bestStart = currentStart

    print("bestStart : " , bestStart)
    print("bestEnd : " , bestEnd)
    
