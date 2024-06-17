'''
Created on 01-Oct-2019

@author: anpradha
Connected Components in an undirected graph
Given an undirected graph, print all connected components line by line. 

Finding connected components for an undirected graph is an easier task. We simple need to do either BFS or DFS starting from every unvisited vertex, 
and we get all strongly connected components. 
Below are steps based on DFS.

1) Initialize all vertices as not visited.
2) Do following for every vertex 'v'.
       (a) If 'v' is not visited before, call DFSUtil(v)
       (b) Print new line character

DFSUtil(v)
1) Mark 'v' as visited.
2) Print 'v'
3) Do following for every adjacent 'u' of 'v'.
     If 'u' is not visited, then recursively call DFSUtil(u)


Time complexity of above solution is O(V + E) as it does simple DFS for given graph.

'''

def DFSUtil(graph,vertex, visited, temp_all_connected_componet):
    
    # set the vertex to visited 
    visited[vertex] = True
    
    temp_all_connected_componet.append(vertex)
    
    for connected_vertex in graph[vertex]:
        if visited[connected_vertex] == False:
            DFSUtil(graph,connected_vertex, visited , temp_all_connected_componet)
    
    return temp_all_connected_componet

def printAllConnectedVertex(graph):
    
    visited = [False for _ in graph.keys()]
    all_connected_componet = []
    
    for vertex in graph.keys():
        temp_all_connected_componet = []
        if visited[vertex] == False:
            temp = DFSUtil(graph,vertex, visited, temp_all_connected_componet)
            all_connected_componet.append(temp)
    
    print("All connected component  : " , all_connected_componet)        
if __name__ == '__main__':
    g = {
     0: [1, 2],
     1: [0],
     2: [0],
     3: [4],
     4: [3]
    }
    printAllConnectedVertex(g)
    
    
