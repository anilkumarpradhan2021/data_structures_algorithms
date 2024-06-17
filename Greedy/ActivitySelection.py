'''
Created on 14-Sep-2016

@author: anpradha
'''
'''

you are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
Example:

Consider the following 6 activities. 
     start[]  =  {1, 3, 0, 5, 8, 5};
     finish[] =  {2, 4, 6, 7, 9, 9};
The maximum set of activities that can be executed 
by a single person is {0, 1, 3, 4}



Solution :
The greedy choice is to always pick the next activity whose finish time is least among the remaining activities and 
the start time is more than or equal to the finish time of previously selected activity. 
We can sort the activities according to their finishing time so that we always consider the next activity as minimum finishing time activity.

1) Sort the activities according to their finishing time
2) Select the first activity from the sorted array and print it.
3) Do following for remaining activities in the sorted array.
…….a) If the start time of this activity is greater than the finish time of previously selected activity then select this activity and print it.
'''


''' Prints a maximum set of activities that can be done by a single person, one at a time.'''


''' it is assumed that the activities are already sorted according to their finish time. '''

if __name__ == '__main__':
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    
    ''' The first activity always gets selected so print it '''
    i = 0 
    print(i, end=" ")
    last_finish = finish[i]
    ''' Consider rest of the activities '''
    for i in range(1, len(finish)):
        ''' If this activity has start time greater than or equal to the finish time of previously selected activity, then select it'''
        if start[i] >= last_finish:
            print(i, end=" ")
            last_finish = finish[i]
            
