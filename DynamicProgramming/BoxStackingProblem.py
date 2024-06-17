'''
Created on 18-Nov-2019

@author: anpradha



Box Stacking Problem | DP-22

You are given a set of n types of rectangular 3-D boxes, where the i^th box has height h(i), width w(i) and depth d(i) (all real numbers). 
You want to create a stack of boxes which is as tall as possible, but you can only stack a box on top of another box 
if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box. 
Of course, you can rotationate a box so that any side functions as its base. It is also allowable to use multiple instances of the same type of box.

https://www.geeksforgeeks.org/box-stacking-problem-dp-22/

https://www.youtube.com/watch?v=9mod_xRB-O0&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=26

Following is the solution based on DP solution of LIS problem.

1) Generate all 3 rotationations of all boxes. The size of rotationation array becomes 3 times the size of original array. For simplicity, we consider depth as always greater than or equal to width.

2) Sort the above generated 3n boxes in decreasing order of base area.

3) After sorting the boxes, the problem is same as LIS with following optimal substructure property.
maxStackHeight(i) = Maximum possible Stack Height with box i at top of stack
maxStackHeight(i) = { Max ( maxStackHeight(j) ) + height(i) } where j < i and width(j) > width(i) and depth(j) > depth(i).
If there is no such j then maxStackHeight(i) = height(i)

4) To get overall maximum height, we return max(maxStackHeight(i)) where 0 < i < n


'''


class Box: 
      
    # Representation of a box 
    def __init__(self, h, w, d): 
        self.h = h 
        self.w = w 
        self.d = d 
    
    def __repr__(self):
        return str([self.d, self.h, self.w])
    

def maxStackHeight(arr, n): 
  
    # Create an array of all rotationations of  
    # given boxes. For example, for a box {1, 2, 3},  
    # we consider three instances{{1, 2, 3}, 
    # {2, 1, 3}, {3, 1, 2}} 
    rotation = [Box(0, 0, 0) for _ in range(3 * n)] 
    index = 0
  
    for i in range(n): 
  
        # Copy the original box 
        rotation[index].h = arr[i].h 
        rotation[index].d = max(arr[i].d, arr[i].w) 
        rotation[index].w = min(arr[i].d, arr[i].w) 
        index += 1
  
        # First rotationation of the box 
        rotation[index].h = arr[i].w 
        rotation[index].d = max(arr[i].h, arr[i].d) 
        rotation[index].w = min(arr[i].h, arr[i].d) 
        index += 1
  
        # Second rotationation of the box 
        rotation[index].h = arr[i].d 
        rotation[index].d = max(arr[i].h, arr[i].w) 
        rotation[index].w = min(arr[i].h, arr[i].w) 
        index += 1
    
    # Now the number of boxes is 3n 
    n *= 3
    
    # Sort the array 'rotation[]' in non-increasing  
    # order of base area 
    rotation.sort(reverse=True , key=lambda a: a.d * a.w)     
    print(rotation)    

    # Initialize maxStackHeight values for all indexes 
    # maxStackHeight[i] --> Maximum possible Stack Height  
    # with box i on top 
    maxStackHeight = [0] * n 
    
    for i in range(n): 
        maxStackHeight[i] = rotation[i].h 
    
    print(maxStackHeight)    

    # Compute optimized maxStackHeight values 
    # in bottom up manner 
    for i in range(1, n): 
        for j in range(0, i): 
            if (rotation[i].w < rotation[j].w and 
                rotation[i].d < rotation[j].d): 
                if maxStackHeight[i] < maxStackHeight[j] + rotation[i].h: 
                    maxStackHeight[i] = maxStackHeight[j] + rotation[i].h       

    print(maxStackHeight)    


if __name__ == '__main__':
    arr = [Box(4, 6, 7), Box(1, 2, 3),
           Box(4, 5, 6), Box(10, 12, 32)] 
    n = len(arr) 
    print("The maximum possible height of stack is",
           maxStackHeight(arr, n)) 
