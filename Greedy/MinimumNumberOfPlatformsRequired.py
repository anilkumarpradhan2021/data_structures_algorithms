'''
Created on 14-Sep-2016

@author: anpradha
'''

'''
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required 
for the railway station so that no train waits.

We are given two arrays which represent arrival and departure times of trains that stop

Examples:
Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)

We can solve the above problem in O(nLogn) time. The idea is to consider all events in sorted order. Once we have all events in sorted order, 
we can trace the number of trains at any time keeping track of trains that have arrived, but not departed.

For example consider the above example.
arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}

All events sorted by time.
Total platforms at any time can be obtained by subtracting total 
departures from total arrivals by that time.
 Time     Event Type     Total Platforms Needed at this Time                               
 9:00       Arrival                  1
 9:10       Departure                0
 9:40       Arrival                  1
 9:50       Arrival                  2
 11:00      Arrival                  3 
 11:20      Departure                2
 11:30      Departure                1
 12:00      Departure                0
 15:00      Arrival                  1
 18:00      Arrival                  2 
 19:00      Departure                1
 20:00      Departure                0

Minimum Platforms needed on railway station = Maximum platforms 
                                              needed at any time 
                                           = 3  
                                           

'''


def findTheMinimumNumberOfPlatformRequired(arrival_time, departure_time):
    ''' Sort arrival and departure arrays'''
    departure_time = sorted(departure_time)
    arrival_time = sorted(arrival_time)
    
    arrival_index = 0
    departure_index = 0
    
    total_train = len(arrival_time)
   
    number_of_platform = 0
    minimum_of_platform = 0
    while arrival_index < total_train and departure_index < total_train :
        ''' Train arrived but not departure'''
        if arrival_time[arrival_index] < departure_time[departure_index]:
            number_of_platform = number_of_platform + 1
            arrival_index = arrival_index + 1
            
        # Train departure 
        else:
            number_of_platform = number_of_platform - 1
            departure_index = departure_index + 1
        ''' Check for the minimum number of platform required or maximum number of train at any time'''
            
        if number_of_platform > minimum_of_platform :
            minimum_of_platform = number_of_platform
            
    print("minimum_of_platform with O(nLogn): " + str(minimum_of_platform))          


''' One more Approach  Complexity O(n) , but space complexity is O(n) '''

def findTheMinimumNumberOfPlatformRequired2(arrival_time, departure_time):
    # Define an aux array
    count = [0 for x in range(2001)]
    
    # For all arrival position add +1
    for i in range(len(arrival_time)):
        count[arrival_time[i]] = count[arrival_time[i]] + 1
    
    # For all departure sub -1
    for i in range(len(departure_time)):
        count[departure_time[i]] = count[departure_time[i]] - 1
    
    minimum_platform = 0
    platform = 0
    
    
    # Just travel the count array and add all the values in respective position
    for i in range(len(count)):
        # platform = platform + count[i]
        # if platform > minimum_platform :
        #     minimum_platform = platform
        minimum_platform = max(count[i],minimum_platform+count[i])
    print("minimum_of_platform with O(n): " + str(minimum_platform))          
        
    
if __name__ == '__main__':
    arrival_time = [900, 940, 950, 1100, 1500, 1800]
    departure_time = [910, 1200, 1120, 1130, 1900, 2000]

    findTheMinimumNumberOfPlatformRequired(arrival_time, departure_time)
    
    findTheMinimumNumberOfPlatformRequired2(arrival_time, departure_time)

