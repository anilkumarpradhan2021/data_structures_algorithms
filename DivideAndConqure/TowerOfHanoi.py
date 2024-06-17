'''
Created on 18-Sep-2016

@author: anpradha
'''


'''

These rings are of different sizes and stacked upon in ascending order i.e. the smaller one sits over the larger one.
There are other variations of puzzle where the number of disks increase, but the tower count remains the same.

Rules
The mission is to move all the disks to some another tower without violating the sequence of arrangement. The below mentioned are few rules which are to be followed for tower of hanoi −

1. Only one disk can be moved among the towers at any given time.
2 .Only the "top" disk can be removed.
3. No large disk can sit over a small disk.

To write an algorithm for Tower of Hanoi, first we need to learn how to solve this problem with lesser amount of disks, say → 1 or 2. We mark three towers with name, source, destination and aux (only to help moving disks). If we have only one disk, then it can easily be moved from source to destination peg.

If we have 2 disks −

1 .First we move the smaller one (top) disk to aux peg
2. Then we move the larger one (bottom) disk to destination peg
3. And finally, we move the smaller one from aux to destination peg.

So now we are in a position to design algorithm for Tower of Hanoi with more than two disks. We divide the stack of disks in two parts. The largest disk (nth disk) is in one part and all other (n-1) disks are in second part.

Our ultimate aim is to move disk n from source to destination and then put all other (n-1) disks onto it. Now we can imagine to apply the same in recursive way for all given set of disks.

So steps to follow are −

Step 1 − Move n-1 disks from source to aux
Step 2 − Move nth disk from source to dest
Step 3 − Move n-1 disks from aux to dest


START
Procedure Hanoi(disk, source, dest, aux)

   IF disk == 0, THEN
      move disk from source to dest             
   ELSE
      Hanoi(disk - 1, source, aux, dest)     // Step 1
      move disk from source to dest          // Step 2
      Hanoi(disk - 1, aux, dest, source)     // Step 3
   END IF
   
END Procedure
STOP
'''
if __name__ == '__main__':
    pass