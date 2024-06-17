'''
Created on 04-Sep-2016

@author: anpradha
'''

'''
// Print all permutations of str in sorted order

'''
def sortedPermutations(arr):
    isFinished = False
    '''
        print this permutation
        
        '''
    print(arr)    
    
    while not isFinished :
        '''
          I) Find the rightmost character which is smaller than its next character. Let us call it 'first char'
        '''
        i = len(arr) - 1
        while i > 0 :
            if arr[i] > arr[i - 1]:
                break
            i = i - 1
        
        '''
        // If there is no such chracter, all are sorted in decreasing order,
        // means we just printed the last permutation and we are done.
        '''
        if i == 0 :
            isFinished = True
        else:
            ''' 
            II) Find the ceil of 'first char' in right of first character. Ceil of a character is the smallest character greater than it
            '''    
            x = arr[i - 1]
            smallest = i; 
            for j in range(i, len(arr) , 1):
                if arr[j] > x and arr[j] < arr[smallest]:
                    smallest = j
            
            
            '''
            III) Swap first and second characters
            '''
            arr[i - 1], arr[smallest] = arr[smallest], arr[i - 1]
            
            '''
            IV) Sort the string on right of 'first char'
            '''
            a = list(sorted(arr[i :]))
            arr = arr[:i ] + a
            print(arr)


if __name__ == "__main__":
    arr = list("ABCA")
    '''
    Sort the string first
    '''
    arr.sort()
    sortedPermutations(arr)