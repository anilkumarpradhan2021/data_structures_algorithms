'''
Created on 25-Sep-2016

@author: anpradha
'''
import operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return " X : " + str(self.x) + " And Y : " + str(self.y)    
        
    
if __name__ == '__main__':
    points = [Point(1, 2), Point(0, 0), Point(3, 6), Point(4, 7)]
    print(points)
    
    print("Sort by lambda function")
    points1 = sorted(points, key=lambda x : x.x)
    print(points1)
    
    
    print("Sorted By Using operator ")
    points2 = sorted(points, key=operator.attrgetter("y"))
    print(points2)
    
    print("Filter element where x > 0 and y > 0")
    points3 = list(filter(lambda pt: pt.x > 0 and pt.y > 0, points))
    print(points3)

