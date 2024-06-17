'''
Created on 07-Oct-2016

@author: anpradha
Problem : Connectivity in a directed graph

Given a directed graph, find out whether the graph is strongly connected or not. A directed graph is strongly connected 
if there is a path between any two pair of vertices.

Undirected Graph :
It is easy for undirected graph, we can just do a BFS and DFS starting from any vertex. If BFS or DFS visits all vertices, then the given undirected graph is connected. 
This approach won’t work for a directed graph.

Directed Graph :
How to do for directed graph?
A simple idea is to use a all pair shortest path algorithm like Floyd Warshall or find Transitive Closure of graph. 
Time complexity of this method would be O(v3).

We can also do DFS V times starting from every vertex. If any DFS, doesn’t visit all vertices, 
then graph is not strongly connected. This algorithm takes O(V*(V+E)) time which can be same as transitive closure
for a dense graph.

A better idea can be Strongly Connected Components (SCC) algorithm. We can find all SCCs in O(V+E) time. 
If number of SCCs is one, then graph is strongly connected. The algorithm for SCC does extra work as it finds all SCCs.

Following is Kosaraju’s DFS based simple algorithm that does two DFS traversals of graph:
1) Initialize all vertices as not visited.

2) Do a DFS traversal of graph starting from any arbitrary vertex v. If DFS traversal doesn’t visit all vertices, then return false.

3) Reverse all arcs (or find transpose or reverse of graph)

4) Mark all vertices as not-visited in reversed graph.

5) Do a DFS traversal of reversed graph starting from same vertex v (Same as step 2). If DFS traversal doesn’t visit all vertices, then return false. Otherwise return true.

'''

def dfs(graph):
    ''' queue for tracking if vertex is visited or not'''
    visited = {v:False for v in graph.keys()}
    
    
    for vertex in graph.keys():
        if visited[vertex] == False:
            dfsUtil(graph, vertex, visited)
    

def dfsUtil(graph, vertex, visited):
    visited[vertex] = True
    
    # print(vertex, end=" ")
    for v in graph[vertex]:
        if visited[v] == False:
            dfsUtil(graph, v, visited)


def traspose_graph(graph):
    temp = {v:[] for v in graph}
    
    for v in graph:
        for u in graph[v]:
            temp[u] = temp[u] + [v] 
            
    
    return temp       


def checkForStronglyConnectedVertex(graph):
    print("checkForStronglyConnectedVertex : ")
    print(graph)
    
    ''' step-1  Mark all the vertices as not visited (For first DFS) '''
    
    visited = {v:False for v in graph.keys()}
    
    ''' Step 2:  take any vertex  so  , Do DFS traversal starting from first vertex.'''
    vertex = graph[0][0]
    dfsUtil(graph, vertex, visited)

    ''' If DFS traversal doesn’t visit all vertices, then return false. '''
    for v in graph:
        for u in graph:
            if visited[u] == False:
                print("Not strongly connected")
                return False
                
    
    '''Step 3: Create a reversed graph '''    
    graph = traspose_graph(graph)
    
    '''Step 4: Mark all the vertices as not visited (For second DFS)'''
    visited = {v:False for v in graph.keys()}
    
    ''' Step 5: Do DFS for reversed graph starting from first vertex.
    Staring Vertex must be same starting point of first DFS'''
    vertex = graph[0][0]
    dfsUtil(graph, vertex, visited)
    
    ''' If DFS traversal doesn’t visit all vertices, then return false. '''
    
    for v in graph:
        for u in graph:
            if visited[u] == False:
                print("Not strongly connected")
                return False
    
    return True        
        
    
 
if __name__ == '__main__':
    g = {
     0: [1],
     1: [2],
     2: [3, 4],
     3: [0],
     4: [2]
    }
    print(checkForStronglyConnectedVertex(g))
    
    g1 = {
     0: [1],
     1: [2],
     2: [3],
     3: []
    }
    print(checkForStronglyConnectedVertex(g1))
