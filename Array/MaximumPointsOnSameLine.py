'''
Created on 19-Nov-2019

@author: anpradha

Count maximum points on same line
Given N point on a 2D plane as pair of (x, y) co-ordinates, we need to find maximum number of point which lie on the same line.

Examples:

Input : points[] = {-1, 1}, {0, 0}, {1, 1}, 
                    {2, 2}, {3, 3}, {3, 4} 
Output : 4
Then maximum number of point which lie on same
line are 4, those point are {0, 0}, {1, 1}, {2, 2},
{3, 3}


Logic Simple :
2 points are on same line if they share same slope 
slope = y2-y2 // x2 -x1
Need to check for if duplicate points .


https://www.geeksforgeeks.org/count-maximum-points-on-same-line/

Not working , but know the logic need to fix it 
'''


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def findMaxiumPointsOnSameLine(arr):
    d = {}
    max_points = 0
    vertical_points = 0
    overlap_points = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ''' if x and y of both point same then overlap'''
            if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                overlap_points = overlap_points + 1
            
            # ''' both have same x co-ordinate'''
            elif arr[i][0] == arr[j][0]:
                vertical_points = vertical_points + 1 
            
            else:
                x_co_diff = arr[j][0] - arr[i][0]
                y_co_diff = arr[j][1] - arr[i][1]
                gcd_of_x_co_y_co = gcd(x_co_diff, y_co_diff)
                key = (y_co_diff / gcd_of_x_co_y_co, x_co_diff / gcd_of_x_co_y_co)
                d[key] = d.get(key, 0) + 1
            max_points = max(d.values())
            max_points = max(max_points, vertical_points)        

    ''' Y overlap +  1 because we selected the point and calculate everything but we dint add it before and similar points to this '''
    max_points = max(max_points, max_points + overlap_points + 1)        
    print(d)
    print("max_points on same Line :  " , max_points)
    print("vertical_points :  " , vertical_points)
    print("overlap_points : " , overlap_points)


if __name__ == '__main__':
    arr = [[-1, 1] , [0, 0], [1, 1], [2, 2], [3, 3] , [3, 4]]
    findMaxiumPointsOnSameLine(arr)
