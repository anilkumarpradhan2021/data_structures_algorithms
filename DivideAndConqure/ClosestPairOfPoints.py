'''
Created on 25-Sep-2016

@author: anpradhas

Problme :

We are given an array of n points in the plane, and the problem is to find out the closest pair of points in the array.
This problem arises in a number of applications. For example, in air-traffic control, you may want to monitor planes that
come too close together, since this may indicate a possible collision.
Recall the following formula for distance between two points p and q.

Following are the steps followed in this algo.

1) We sort all points according to x coordinates.

2) Divide all points in two halves. (left, right)

3) Recursively find the smallest distances in both subarrays.

4) Take the minimum of two smallest distances. Let the minimum be d.

5) Create an array strip[] that stores all points which are at most d distance away from the middle line dividing the two sets.

6) sort strip[] by y axis .

7) Find the smallest distance in strip[].


Complexity : O(nLogn) 

'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return " X : " + str(self.x) + " And Y : " + str(self.y)    


'''  distance between 2 points formula sqrt root of ( (X2-X1)^2 + (Y2-Y1)^2 ) '''        
def distance_points(point1, point2):
    return abs((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** .5 


def closePoints(points):
    n = len(points)
    
    if n <= 1:
        raise Exception("One point not enough")
    
    # If there are 2 or 3 points, then use brute force
    elif n == 2:
        return (points[0], points[1]) 
    
    elif n == 3 :
        ''' 1st compare a and b then compare the result with b and c ''' 
        (a , b , c) = points
        result = (a, b) if distance_points(a, b) < distance_points(a, c) else (a, c)
        result = (result[0], result[1]) if distance_points(result[0], result[1]) < distance_points(b, c) else (b, c)
        return result
    
    else:
        ''' 
        Step -1
        sort by x coordinates 
        '''
        points = sorted(points, key=lambda x: x.x)
        
        ''' 
        Step-2
        divide into 2 parts like left and right
        '''
        leftPoints = points[:n // 2]
        rightPoints = points[n // 2:]
        
        '''
            Step-3
            recursive division
            
        '''
        
        left_a, left_b = closePoints(leftPoints)
        right_a, right_b = closePoints(rightPoints)

        
        '''step-4
        find the minimum distance of a pair of points from 2 half
        
        Recursively find the smallest distances in both subarrays. Let the distances be dl and dr.
        Find the minimum of dl and dr. Let the minimum be d.
        
         '''
        d = min(distance_points(left_a, left_b), distance_points(right_a, right_b))
        
        ''' Syep-5 find the median in x axis'''

        print(points)
        mid = (points[n // 2].x + points[n // 2 + 1].x) // 2
        
        '''Step -6 , find all the points in the range between [mid -d to mid + d] '''
        
        midRange = filter(lambda pt:pt.x >= mid - d and pt.x <= mid + d, points)
        
        
        '''Step -7 resultant sort by y axis  '''

        midRange = sorted(midRange, key=lambda x : x.y)
        
        result = None  # to store the points
        localMin = float('inf')  # set it to infinite 
        
        ''' find the closet points using brute force for each point with each other points
            maximum number of compare for a particular point is 7 
        '''
        for i in range(len(midRange)):
            a = midRange[i]
            for j in range(i + 1, len(midRange)):
                b = midRange[j]
                if (a.y - b.y <= d) and distance_points(a, b) < localMin:
                    localMin = distance_points(a, b)
                    result = (a, b)
                
        return result
        
        
    
        
if __name__ == '__main__':
    points = [Point(1, 2), Point(0, 0), Point(3, 6), Point(4, 7), Point(5, 5), Point(8, 4), Point(2, 9), Point(4, 5), Point(8, 1), Point(4, 3), Point(3, 3)]
    # points = [Point(1, 2), Point(0, 0), Point(3, 6), Point(4, 7), Point(5, 5)]
    
    print(closePoints(points))
    
