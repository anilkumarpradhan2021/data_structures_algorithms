'''
Created on 23-Nov-2019

@author: anpradha
Rank of an element in a stream
Given a stream of integers, lookup the rank of a given integer x. Rank of an integer in stream is “Total number of elements less than or equal to x (not including x)”.

If element is not found in stream or is smallest in stream, return -1.
Examples:

Input :  arr[] = {10, 20, 15, 3, 4, 4, 1}
              x = 4;
Output : Rank of 4 in stream is: 3
There are total three elements less than
or equal to x (and not including x)

Input : arr[] = {5, 1, 14, 4, 15, 9, 7, 20, 11}, 
           x = 20;
Output : Rank of 20 in stream is: 8


An efficient way is to use a Binary Search Tree. Each Node will hold the data value and size of its left subtree.

We traverse the tree from root and compare the root values to x.

If root->data == x, return size of left subtree of root.
If x < data, return getRank(root->left)
If x > root->data, return getRank(root->right) + size of letSubtree + 1.

https://www.geeksforgeeks.org/rank-element-stream/


'''


class newNode: 

    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None
        self.leftSize = 0

  
# Inserting a new Node.  
def insert(root, data): 
    if root == None:  
        return newNode(data)  
  
    # Updating size of left subtree.  
    if data <= root.data:  
        root.left = insert(root.left, data)  
        root.leftSize += 1
    else: 
        root.right = insert(root.right, data) 
    return root 

  
# Function to get Rank of a Node x.  
def getRank(root, x): 
      
    # Step 1.  
    if root.data == x: 
        return root.leftSize  
  
    # Step 2.  
    if x < root.data:  
        if root.left == None:  
            return -1
        else: 
            return getRank(root.left, x) 
  
    # Step 3.  
    else:  
        if root.right == None:  
            return -1
        else:  
            rightSize = getRank(root.right, x)  
            return root.leftSize + 1 + rightSize 

  
# Driver code  
if __name__ == '__main__': 
    arr = [5, 1, 4, 4, 5, 9, 7, 13, 3]  
    n = len(arr)  
    x = 4
  
    root = None
    for i in range(n): 
        root = insert(root, arr[i]) 
  
    print("Rank of", x, "in stream is:",
                       getRank(root, x)) 
    x = 13
    print("Rank of", x, "in stream is:",
                       getRank(root, x)) 
  
# This code is contributed by PranchalK 
