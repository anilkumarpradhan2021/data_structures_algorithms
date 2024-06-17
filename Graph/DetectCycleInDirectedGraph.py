'''
@author: anpradha

Created on 04-Oct-2016
Problem : Detect Cycle in a Directed Graph

Given a directed graph, check whether the graph contains a cycle or not. Your function should return true 
if the given graph contains at least one cycle, else return false. For example, 
the following graph contains three cycles 0->2->0, 0->1->2->0 and 3->3, so your function must return true.

Complexity : O(V+E).

Depth First Traversal can be used to detect cycle in a Graph.
'''

def dfs_util(graph, vertex, visited):
    visited[vertex] = True
    
    for adj_vertex in graph[vertex]:
        if visited[adj_vertex] == True:
            print("Cycle detected in Graph")
            return
        dfs_util(graph, adj_vertex, visited)
            
        
        
def dfs(graph):
    print("graph: " + str(graph))
    visited = {key:False for key in graph.keys()}
    
    for vertex in graph.keys():
        if visited[vertex] == False:
            dfs_util(graph, vertex, visited)

def dfs2(graph):
    visited = {key:False for key in graph.keys()}
    for node in graph.keys():
        for vertices in graph[node]:
            if visited[vertices] == True:
                print("Cycle")
                break
            else:
                visited[vertices] = True
      
if __name__ == '__main__':
    g = {
         1: [2, 3],
         2: [3],
         3: [] 
        }
    dfs(g)

    g1 = {
         1: [2],
         2: [3],
         3: [] 
        }
    dfs(g1)
    dfs2(g)
