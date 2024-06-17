'''
Created on 09-Oct-2016

@author: anpradha

Problem : Eulerian path and circuit for undirected graph

Eulerian Cycle
An undirected graph has Eulerian cycle if following two conditions are true.
….a) All vertices with non-zero degree are connected. We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path (we only consider all edges).
….b) All vertices have even degree.

Eulerian Path
An undirected graph has Eulerian Path if following two conditions are true.
….a) Same as condition (a) for Eulerian Cycle
….b) If zero or two vertices have odd degree and all other vertices have even degree. Note that only one vertex with odd degree is not possible in an undirected graph (sum of all degrees is always even in an undirected graph)

Note that a graph with no edges is considered Eulerian because there are no edges to traverse.


'''


def isConnected(graph):
    '''Mark all the vertices as not visited and not part of recursion'''
    visited = {v:False for v in graph}

    '''find a vertex with number of adjacent vertex greater than 1 '''
    for v in graph:
        if len(graph[v]) > 0:
            starting_point = v
            break
    
    '''Start DFS traversal from a vertex with non-zero degree'''
    dfsUtil(graph, starting_point, visited)
    
    '''Check if all non-zero degree vertices are visited'''
    for v in graph:
        if len(graph[v]) > 0 and visited[v] == False:
            return False
    
    return True    
    

def dfsUtil(graph, vertex, visited):
    
    '''Mark the current node as visited'''
    visited[vertex] = True
    
    '''  Recur for all the vertices adjacent to this vertex '''
    for u in graph[vertex]:
        
        ''' If an adjacent is not visited, then recur for that adjacent '''
        if visited[u] == False:
            dfsUtil(graph, u, visited)

def isEulerian(graph):
    ''' step-1 Check if all non-zero degree vertices are connected '''
    if isConnected(graph) == False:
        print("All non-zero degree vertices are not connected")
        
    number_of_odd_degree_vertex = 0
    
    '''Count vertices with odd degree'''
    for v in graph:
        if len(graph[v]) & 1 == 1:
            number_of_odd_degree_vertex = number_of_odd_degree_vertex + 1
            
    print("number_of_odd_degree_vertex : " + str(number_of_odd_degree_vertex))        
            
    if number_of_odd_degree_vertex == 0:
        print("Its a Eulerian Circuit")
    elif number_of_odd_degree_vertex == 2:
        print("Its a Eulerian path")
    else:
        print("Its not a Eulerian path or Eulerian Circuit")    
      
  
if __name__ == '__main__':
    g1 = {
     0: [1, 2, 3],
     1: [0, 2],
     2: [1, 0],
     3: [0, 4],
     4: [3]
    }
    isEulerian(g1)


    g2 = {
     0: [1, 3],
     1: [0, 2],
     2: [1, 0],
     3: [0, 4],
     4: [0, 3]
    }
    isEulerian(g2)

    g3 = {
     0: [1, 2, 3],
     1: [0, 2, 3],
     2: [1, 0],
     3: [0, 1, 4],
     4: [0, 3]
    }
    isEulerian(g3)
