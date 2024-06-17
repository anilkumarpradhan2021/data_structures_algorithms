'''
Created on 04-Oct-2016

@author: anpradha

Problem :
1 . We want to find a minimum spanning tree for a connected weighted undirected graph. 


Kruskal’s Minimum Spanning Tree Algorithm

What is Minimum Spanning Tree?
Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all 
the vertices together. A single graph can have many different spanning trees. A minimum spanning tree (MST) 
or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with weight less 
than or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given 
to each edge of the spanning tree.

How many edges does a minimum spanning tree has?
A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.

Below are the steps for finding MST using Kruskal’s algorithm

1. Sort all the edges in non-decreasing order of their weight.

2. Pick the smallest edge. Check if it forms a cycle with the spanning tree 
formed so far. If cycle is not formed, include this edge. Else, discard it.  

3. Repeat step#2 until there are (V-1) edges in the spanning tree.


DISJOINT SET :
A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into a number of 
disjoint (non-overlapping) subsets. A union-find algorithm is an algorithm that performs two useful operations on such
 a data structure:

Find: Determine which subset a particular element is in. This can be used for determining if two elements are 
in the same subset.

Union: Join two subsets into a single subset.

'''


parent = {}
rank = {}

''' initially parent of the vertex is vertex itself '''
def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0


''' A utility function to find set of an element i  (Uses path compression technique) '''
def find_vertex(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find_vertex(parent[vertex])
    return parent[vertex] 

'''
A function that does union of two sets of x and y (Uses union by Rank) '''

def union(vertex1, vertex2): 
    root1 = find_vertex(vertex1) 
    root2 = find_vertex(vertex2)
    
    if root1 != root2:
        
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        
        elif rank[root1] < rank[root2]:
            parent[root1] = root2

        else:
            parent[root1] = root2
            rank[root2] = rank[root2] + 1    
            
      
def kruskal(graph):
    print("All vertices are :")
    vertices = graph["vertices"]
    edges = graph["edges"]
    print(vertices)
    
    final_minimal_spanning_tree = []
    
    '''step-1 Create vertices set '''
    for vertex in vertices:
        make_set(vertex)
    
    ''' step-2 sort the edges'''
    edges.sort()   
    
    for edge in edges:
        weight , vertex1 , vertex2 = edge
        
        ''' find the parent of both vertex , if both parents are same means both are in same set else in different set'''
        root1 = find_vertex(vertex1)
        root2 = find_vertex(vertex2)
        if root1 != root2:
            union(vertex1, vertex2)
            final_minimal_spanning_tree.append(edge)
        
    print(final_minimal_spanning_tree)
    
if __name__ == '__main__':
    graph = {
            'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
            'edges': [(1, 'A', 'B'), (5, 'A', 'C'), (3, 'A', 'D'), (4, 'B', 'C'), (2, 'B', 'D'), (1, 'C', 'D'), ]
            }
    
    kruskal(graph)
