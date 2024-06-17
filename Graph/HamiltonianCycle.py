'''
Created on 10-Oct-2016

@author: anpradha


Note: 
An Euler path is a path that crosses every edge exactly once without repeating, if it ends at the initial vertex then it is a Euler cycle.

A Hamiltonian path passes through each vertex (note not each edge), exactly once, if it ends at the initial vertex then it is a Hamiltonian cycle.

In a Euler path you might pass through a vertex more than once.

In a Hamiltonian path you may not pass through all edges.


Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once. A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path such 
that there is an edge (in graph) from the last vertex to the first vertex of the Hamiltonian Path. Determine whether a given graph contains Hamiltonian Cycle or not. 
If it contains, then print the path. Following are the input and output of the required function

Backtracking Algorithm
Create an empty path array and add vertex 0 to it. Add other vertices, starting from the vertex 1. Before adding a vertex, check for whether it is adjacent
 to the previously added vertex and not already added. 

If we find such a vertex, we add the vertex as part of the solution. If we do not find a vertex then we return false.


Condition : 1
All vertex should be covered 

Condition : 2
Last vertex should have connection with 1st vertex 

'''


def hamCycle(graph):
    
    start = list(graph.keys())[0]
    path = [-1 for v in graph]
    path[0] = start
    visited = {v:False for v in graph}
    visited[start] = True
    
    if hamCycleUtil(graph, path, 1, visited) == True:
        print("Path exists")
        print(path + [path[start]])
    else:
        print("Path  does not exists") 
         

def hamCycleUtil(graph, path, pos, visited):
    
    '''Condition -1: Base case : If all vertices are included in Hamiltonian Cycle '''
    if pos == len(graph):
        end_vertex = path[-1]
        start_vertex = path[0]
        ''' Condition -2 And if there is an edge from the last included vertex to the first vertex'''
        if end_vertex in graph[start_vertex]:
            return True
        else:
            return False
    
    for v in range(1, len(graph)):
        '''Check if this vertex can be added to Hamiltonian Cycle'''

        if isSafe(graph, path, pos, v, visited):
            path[pos] = v
            visited[path[pos]] = True
            
            '''recur to construct rest of the path'''
            if hamCycleUtil(graph, path, pos + 1, visited) == True:
                return True
            
            print("Backtarck")
            print(path)
            
            '''If adding vertex v doesn't lead to a solution,then remove it'''
            visited[path[pos]] = False
            path[pos] = -1
        
    return False         

def isSafe(graph, path, pos, v, visited):
    last_vertex_form_path = path[pos - 1]
    if v in graph[last_vertex_form_path] and visited[v] == False:
        return True
    else:
        False
    
if __name__ == '__main__':
    graph = {
              0: {1, 3},
              1: {0, 2, 3, 4},
              2: {1, 4},
              3: {0, 1, 4},
              4: {1, 2, 3},
              }

    hamCycle(graph)
    print("hamiltonain Cycle for 2nd graph")

    graph1 = {
              0: {1, 3},
              1: {0, 2, 3, 4},
              2: {1, 4},
              3: {0, 1},
              4: {1, 2},
              }

    hamCycle(graph1)
