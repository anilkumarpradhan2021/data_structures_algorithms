'''
Created on 10-Oct-2016

@author: anpradha

Problem : Print all paths from a given source to a destination

SAME is done in problem Path exits Between 2 Vertics
'''

def dfs(graph, start_vertex, end_vertex):
    '''Mark all the vertices as not visited and not part of recursion'''
    visited = {v:False for v in graph}

    '''Call the recursive helper function to detect cycle in different DFS trees'''
    dfsUtil(graph, start_vertex, visited, end_vertex, [])


def dfsUtil(graph, start_vertex, visited, end_vertex, path):
    
    '''Mark the current node as visited'''
    visited[start_vertex] = True
    path = path + [start_vertex]
    
    '''  Recur for all the vertices adjacent to this vertex '''
    for u in graph[start_vertex]:
        
        ''' If an adjacent is not visited, then recur for that adjacent '''
        if visited[u] == False:
            dfsUtil(graph, u, visited, end_vertex, path)
        
        if u == end_vertex:
            print(path + [u])
               
        # visited[u] = False

def test(graph,source,dest):
    a = [False for v in graph.keys()]
    path = []
    a[source] = True
    path = path + [source]
    for v1 in graph[source]:
        for v in graph[v1]:
            if a[v] == False:
                a[v] = True
                path = path + [v]
            if v == dest:
                print("found Path : " , path)
                return path
            
    
if __name__ == '__main__':
    g = {
     0: [1, 2],
     1: [0, 2],
     2: [0, 1]
    }
    print(dfs(g, 0, 2))

    g1 = {
     0: [1, 2, 3],
     1: [3],
     2: [3],
     3: []
    }
    print(dfs(g1, 0, 3))
    print(test(g,0,2))
