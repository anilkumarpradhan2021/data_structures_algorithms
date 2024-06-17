'''
Created on 04-Oct-2016

Problem : Detect cycle in an undirected graph


@author: anpradha

DISJOINT SET :
A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into a number of 
disjoint (non-overlapping) subsets. A union-find algorithm is an algorithm that performs two useful operations on such
 a data structure:

Find: Determine which subset a particular element is in. This can be used for determining if two elements are 
in the same subset.

Union: Join two subsets into a single subset.


Complexity : O(Logn)

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
            
      
def isCycleExists(graph):
    print("All vertices are :")
    vertices = graph["vertices"]
    edges = graph["edges"]
    print(vertices)
    
    '''step-1 Create vertices set '''
    for vertex in vertices:
        make_set(vertex)
    
    for edge in edges:
        weight , vertex1 , vertex2 = edge
        
        ''' find the parent of both vertex , if both parents are same means both are in same set else in different set'''
        root1 = find_vertex(vertex1)
        root2 = find_vertex(vertex2)
        if root1 == root2:
            print("Graph contains cycle")
            return
        union(vertex1, vertex2)
        
    print("Graph does not contains cycle")
    
    
if __name__ == '__main__':
    graph = {
            'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
            'edges': [(1, 'A', 'B'), (5, 'A', 'C'), (3, 'A', 'D'), (4, 'B', 'C'), (2, 'B', 'D'), (1, 'C', 'D'), ]
            }
    
    isCycleExists(graph)

    graph1 = {
            'vertices': ['A', 'B', 'C'],
            'edges': [(1, 'A', 'B'), (5, 'A', 'C')]
            }
    
    isCycleExists(graph1)
