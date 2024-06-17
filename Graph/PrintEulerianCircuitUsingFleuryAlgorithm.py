'''
Created on 09-Oct-2016

@author: anpradha

Problem :
Fleury’s Algorithm for printing Eulerian Path or Circuit.


Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit is an Eulerian Path 
which starts and ends on the same vertex.


Bridges in a graph:
An edge in an undirected connected graph is a bridge iff removing it disconnects the graph.
For a disconnected undirected graph, definition is similar, a bridge is an edge removing which increases
 number of connected components.


Following is Fleury’s Algorithm for printing Eulerian trail or cycle (Source Ref1).

1. Make sure the graph has either 0 or 2 odd vertices.

2. If there are 0 odd vertices, start anywhere. If there are 2 odd vertices, start at one of them.

3. Follow edges one at a time. If you have a choice between a bridge and a non-bridge, always choose the non-bridge.

4. Stop when you run out of edges.

ASSUMING WE HAVE CHECKED THE EULERIAN CIRCUIT ELSE WE CAN ADD CODE FOR SAME 
'''

def printEulerTour(graph):
    start = 0
    
    '''Find a vertex with odd degree  NOTE :  if no odd edge then start with 0th vertex as all are even degree'''
    for v in graph:
        if len(graph[v]) & 1 == 1:
            start = v
            break
    
    '''Print tour starting from odd vertex'''   
    printEulerutil(graph, start)    
        

def printEulerutil(graph, v):
    ''' Recur for all the vertices adjacent to this vertex''' 
    for u in graph[v]:
        '''If edge u-v is not removed and it's a a valid next edge'''
        if isValidNextEdge(graph, u, v):
            print(u, v, end=' , ')
            ''' edge considered/printed so delete this edge now'''
            removeEdge(graph, u, v)
            printEulerutil(graph, u)
            


'''The function to check if edge u-v can be considered as next edge in Euler Tour'''    
def isValidNextEdge(graph, adj_vertex, v):
    '''The edge u-v is valid in one of the following two cases:'''
    
    
    '''Case-1 If the vertex have only one adjacent vertex'''
    if len(graph[v]) == 1:
        return True
    
    '''Case -2  Check if u is a bridge '''
    '''2.a) count of vertices reachable from u'''
    
    visited = {v:False for v in graph.keys()}
    count1 = dfsCount(graph, visited, v)
    
    '''2.b) Remove edge (u, v) and after removing the edge, count vertices reachable from u'''
    removeEdge(graph, adj_vertex, v)
    visited = {v:False for v in graph.keys()}
    
    count2 = dfsCount(graph, visited, v)
    
    '''2.c) Add the edge back to the graph'''
    addEdge(graph, adj_vertex, v)
    
    '''2.d) If count1 is greater, then edge (u, v) is a bridge'''
    if count1 > count2 :
        return False
    else:
        return True 
    
'''A DFS based function to count reachable vertices from v'''
def dfsCount(graph, visited, u):
    visited[u] = True
    count = 1
    
    for v in graph[u]:
        
        if visited[v] != True:
            count = count + dfsCount(graph, visited, v)    
    
    return count        


'''This function removes edge u-v from graph.  It removes the edge by replacing adjcent vertex value with -1.'''
def removeEdge(graph, u, v):
    '''Remove v in adjacency list of u '''
    graph[u].remove(v)
    
    '''Remove u in adjacency list of v '''
    graph[v].remove(u)

def addEdge(graph, u, v): 
    graph[u].insert(0, v)
    graph[v].insert(0, u)   
    
    
    
if __name__ == '__main__':
    print("Eulerian Path or Circuit")
    g1 = {
     0: [1, 2],
     1: [0, 2],
     2: [0, 1]
    }
    printEulerTour(g1)
    print("\nEulerian Path or Circuit")

    g2 = {
     0: [2, 1],
     1: [0, 2],
     2: [0, 1, 3],
     3: [2]
    }
    printEulerTour(g2)
