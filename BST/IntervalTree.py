'''
Created on 13-Nov-2016

@author: anpradha



Interval Tree

Consider a situation where we have a set of intervals and we need following operations to be implemented efficiently.
1) Add an interval
2) Remove an interval
3) Given an interval x, find if x overlaps with any of the existing intervals.

Interval Tree: The idea is to augment a self-balancing Binary Search Tree (BST) like Red Black Tree, AVL Tree, etc to maintain set of intervals so that all operations can be done in O(Logn) time.

Every node of Interval Tree stores following information.
a) i: An interval which is represented as a pair [low, high]
b) max: Maximum high value in subtree rooted with this node.

The low value of an interval is used as key to maintain order in BST. The insert and delete operations are same as insert and delete in self-balancing BST used. 


Interval overlappingIntervalSearch(root, x)
1) If x overlaps with root's interval, return the root's interval.

2) If left child of root is not empty and the max  in left child 
is greater than x's low value, recur for left child

3) Else recur for right child.


'''

class Interval(object):
    def __init__(self, low, high):
        self.low_interval = low
        self.high_interval = high
   
    def __str__(self):
        return " low " + str(self.low_interval) + " and high : " + str(self.high_interval)
    
    
class Node(object):
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high_interval
        self.left_child = None
        self.right_child = None

def insert_interval(root, interval):
    
    '''Base case: Tree is empty, new node becomes root'''
    if root is None:
        root = Node(interval)
        return root
    
    '''If root's low value is greater, then new interval goes to left subtree'''
    if interval.low_interval < root.interval.low_interval:
        root.left_child = insert_interval(root.left_child, interval)
    else:
        root.right_child = insert_interval(root.right_child, interval)     
    
    '''Update the max value of this ancestor if needed'''
    root.max = max(root.max, interval.high_interval)     
    return root      

def overlap_search(root, interval):
    if root is None:
        print("No overlap interval found ")
        return 
    
    '''check for overlap with root'''
    if root.interval.low_interval < interval.high_interval and interval.low_interval < root.interval.high_interval :
        print("Overlap Found")
        print(root.interval)
        
    else:
        '''If left child of root is present and max of left child is greater than or equal to given interval, then i may overlap with an interval is left subtree'''
        if root.left_child is not None and interval.low_interval <= root.left_child.max:
            overlap_search(root.left_child, interval)
        else:
            overlap_search(root.right_child, interval)        

def inOrder(root):
    if root is None :
        return
    inOrder(root.left_child)
    print(root.interval)
    #print(root.max)
    inOrder(root.right_child)

if __name__ == '__main__':
    root = None
    root = insert_interval(root, Interval(15, 20))
    insert_interval(root, Interval(10, 30))
    insert_interval(root, Interval(17, 19))
    insert_interval(root, Interval(5, 20))
    insert_interval(root, Interval(12, 15))
    insert_interval(root, Interval(30, 40))
    inOrder(root)
    
    interval_to_search = Interval(6, 7)
    overlap_search(root, interval_to_search)
    
    interval_to_search = Interval(60, 70)
    overlap_search(root, interval_to_search)
    