'''
Created on 20-Nov-2019

@author: anpradha

Program for Point of Intersection of Two Lines
Given points A and B corresponding to line AB and points P and Q corresponding to line PQ, find the point of intersection of these lines. The points are given in 2D Plane with their X and Y Coordinates.

https://www.geeksforgeeks.org/program-for-point-of-intersection-of-two-lines/

EASY JUST READ IT ONCE 

Examples:

Input : A = (1, 1), B = (4, 4)
        C = (1, 8), D = (2, 4)
Output : The intersection of the given lines 
         AB and CD is: (2.4, 2.4)

Input : A = (0, 1), B = (0, 4)
        C = (1, 8), D = (1, 4)
Output : The given lines AB and CD are parallel.


Let the given lines be :

a1x + b1y = c1
a2x + b2y = c2
We have to now solve these 2 equations to find the point of intersection. To solve, we multiply 1. by b2 and 2 by b1
This gives us,
a1b2x + b1b2y = c1b2
a2b1x + b2b1y = c2b1

Subtracting these we get,
(a1b2 – a2b1) x = c1b2 – c2b1

This gives us the value of x. Similarly, we can find the value of y. (x, y) gives us the point of intersection.

Note: This gives the point of intersection of two lines, but if we are given line segments instead of lines, we have to also recheck that the point so computed actually lies on both the line segments.
If the line segment is specified by points (x1, y1) and (x2, y2), then to check if (x, y) is on the segment we have to just check that

min (x1, x2) <= x <= max (x1, x2)
min (y1, y2) <= y <= max (y1, y2)
The pseudo code for the above implementation:

determinant = a1 b2 - a2 b1
if (determinant == 0)
{
    // Lines are parallel
}
else
{
    x = (c1b2 - c2b1)/determinant
    y = (a1c2 - a2c1)/determinant
}


https://www.geeksforgeeks.org/program-find-line-passing-2-points/

Let the given two points be P(x1, y1) and Q(x2, y2). Now, we find the equation of line formed by these points.

Any line can be represented as,
ax + by = c
Let the two points satisfy the given line. So, we have,
ax1 + by1 = c
ax2 + by2 = c
We can set the following values so that all the equations hold true,

a = y2 - y1
b = x1 - x2
c = ax1 + by1
These can be derived by first getting the slope directly and then finding the intercept of the line. OR these can also be derived cleverly by a simple observation as under:

Derivation :

ax1 + by1 = c ...(i)
ax2 + by2 = c ...(ii)
Equating (i) and (ii),
ax1 + by1 = ax2 + by2
=> a(x1 - x2) = b(y2 - y1)
Thus, for equating LHS and RHS, we can simply have,
a = (y2 - y1)
AND
b = (x1 - x2)
so that we have,
(y2 - y1)(x1 - x2) = (x1 - x2)(y2 - y1)
AND
Putting these values in (i), we get,
c = ax1 + by1 
'''



''' I can code it , '''
if __name__ == '__main__':
    points = [[1, 1], [4, 4]]
