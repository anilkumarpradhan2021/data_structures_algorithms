'''
Created on 12-Sep-2016

@author: anpradha

Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently.
Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.

Other way of asking this problem is, given a box with locks and keys where one lock can be opened by one key in the box. We need to match the pair.


'''



'''
Created on 10-May-2016

@author: anpradha



This algorithm first performs a partition by picking last/first element of bolts array as pivot,
Rearrange the array of nuts and returns the partition index ‘i’ such that all nuts smaller than nuts[i] are on the left side and all nuts greater than nuts[i] are on the right side.
Next using the nuts[i] we can partition the array of bolts. 
Partitioning operations can easily be implemented in O(n).
This operation also makes nuts and bolts array nicely partitioned. 
Now we apply this partitioning recursively on the left and right sub-array of nuts and bolts.

As we apply partitioning on nuts and bolts both so the total time complexity will be Θ(2*nlogn) = Θ(nlogn) on average.
 
'''



'''Working for this condition but need to check whether correct or not , duplicate entry not working - fixed it by <= condition'''

def partition(arr, low, high, pivot_element):
        i = low
        j = high

        while i < j :
            while i < high and arr[i] <= pivot_element:
                i = i + 1
                
            while j > low and arr[j] > pivot_element:
                j = j - 1
    
            if i < j:
                ''' Swap '''
                arr[i] , arr[j] = arr[j], arr[i]
        
        ''' Return the partition index of an array based on the pivot element of other array. ''' 
        return j

''' Not working but solution given in geeksandGeeks'''
    
def partition1(arr, low, high, pivot_element):
        i = low
        for j in range(low, high):
            if arr[j] < pivot_element:
                arr[i] , arr[j] = arr[j], arr[i]
                i = i + 1
            elif arr[j] == pivot_element:   
                arr[j] , arr[high] = arr[high], arr[j]
                j = j - 1
    
        arr[high] , arr[i] = arr[i], arr[high]        
        ''' Return the partition index of an array based on the pivot element of other array. '''        
        return i

def quickSort(low, high, nuts, bolts):
    if low < high:
        ''' Choose last/first character of bolts array for nuts partition. '''
        print("nuts")
        pivot = partition(nuts, low, high, bolts[high])
        ''' Now using the partition of nuts choose that for bolts partition.'''
        print("bolts")
        partition(bolts, low, high, nuts[pivot])
        ''' Recur for [low...pivot-1] & [pivot+1...high] for nuts and bolts array. '''
        quickSort(low, pivot - 1, nuts, bolts)
        quickSort(pivot + 1, high, nuts, bolts)

        
if __name__ == "__main__":
    bolts = ['$', '%', '&', '^', '@', '#']
    nuts = ['@', '#', '$', '%', '^', '&']
    bolts = [11, 5, 10, 25, 1,1]
    nuts = [5, 10, 25, 1, 11,1]
    
    # 12, 23, 1, 24, 111, 34, 1, 12, 2 , 2
    print("Print array before sort")
    print("bolts : " + str(bolts))
    print("nuts " +str(nuts))
    print("Print array after sort")
    quickSort(0, len(bolts) - 1, nuts, bolts)
    print("bolts : " + str(bolts))
    print("nuts " +str(nuts))
    
         
