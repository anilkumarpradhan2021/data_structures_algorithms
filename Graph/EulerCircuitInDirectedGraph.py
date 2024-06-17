'''
Created on 09-Oct-2016

@author: anpradha

How to check if a directed graph is eulerian?
A directed graph has an eulerian cycle if following conditions are true (Source: Wiki)
Condition 1) All vertices with nonzero degree belong to a single strongly connected component.
Condition 2) In degree and out degree of every vertex is same.

We can detect singly connected component using Kosaraju’s DFS based simple algorithm.
To compare in degree and out degree, we need to store in degree an out degree of every vertex. 
Out degree can be obtained by size of adjacency list. In degree can be stored by creating an array of size equal 
to number of vertices.

Complexity : O(V + E)

'''



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


def isEulerianCycle(graph):
    
    '''Condition -1 : Check if all non-zero degree vertices are connected '''
    
    if checkForStronglyConnectedVertex(graph) == False:
        print("Its not strongly connected ")
        return False
    
    inDegress = {v:0 for v in graph}
    for v in graph:
        for u in graph[v]:
            inDegress[u] = inDegress[u] + 1
    
    ''' Condition -2 : Check if in degree and out degree of every vertex is same''' 
    for v in graph.keys():
        if len(graph[v]) != inDegress[v]:
            print("in degree and out degree of " + str(v) + "Not same")
            return False
        
    return True    
    
        
if __name__ == '__main__':
    g = {
     0: [3, 2],
     1: [0],
     2: [1],
     3: [4],
     4: [0]
    }
    print(isEulerianCycle(g))
