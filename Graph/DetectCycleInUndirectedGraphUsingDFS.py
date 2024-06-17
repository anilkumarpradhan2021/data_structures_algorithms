'''
Created on 08-Oct-2016

@author: anpradha

Problem:
Detect cycle in an undirected graph

Time Complexity: The program does a simple DFS Traversal of graph and graph is represented using adjacency list. 
So the time complexity is O(V+E)
'''

def dfs(graph):
    '''Mark all the vertices as not visited and not part of recursion'''
    visited = {v:False for v in graph}

    '''Call the recursive helper function to detect cycle in different DFS trees'''
    for v in graph:
        if visited[v] == False:
            return dfsUtil(graph, v, visited, -1)
    return False    


def dfsUtil(graph, vertex, visited, parent):
    
    '''Mark the current node as visited'''
    visited[vertex] = True
    
    
    '''  Recur for all the vertices adjacent to this vertex '''
    for u in graph[vertex]:
        
        ''' If an adjacent is not visited, then recur for that adjacent '''
        if visited[u] == False:
            dfsUtil(graph, u, visited, vertex)
        # If an adjacent is visited and not parent of current vertex, then there is a cycle.    
        else:
            if parent != u:
                return True
    
    return False            
    
if __name__ == '__main__':
    g = {
     0: [1, 2],
     1: [0, 2],
     2: [0, 1]
    }
    print(dfs(g))

    g1 = {
     0: [1, 2],
     1: [0],
     2: [0]
    }
    print(dfs(g1))
