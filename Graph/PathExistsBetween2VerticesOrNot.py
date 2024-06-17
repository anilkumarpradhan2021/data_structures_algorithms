'''
Created on 05-Oct-2016

@author: anpradha

Using DFS we can find if path exist between 2 vertex or not


The idea is to do Depth First Traversal of given directed graph. Start the traversal from source. 
Keep storing the visited vertices in an array say ‘path[]’. If we reach the destination vertex, print contents of path[]. 
The important thing is to mark current vertices in path[] as visited also, so that the traversal doesn’t go in a cycle.

'''

def pathExits(graph, start_vertex, end_vertex):
    print("Path exist between : " + str(start_vertex) + " and " + str(end_vertex))
    
    ''' queue for tracking if vertex is visited or not'''
    visited = {v:False for v in graph.keys()}
    
    ''' multiple path '''
    paths = []
    
    if visited[start_vertex] == False:
        pathExitsUtil(graph, start_vertex, end_vertex, visited, [], paths)
        print(paths)
    

def pathExitsUtil(graph, start_vertex, end_vertext, visited, path, paths):
    visited[start_vertex] = True
    path = path + [start_vertex]
    
    for vertex in graph[start_vertex]:
        if vertex == end_vertext:
            path = path + [end_vertext]
            paths.append(path)
         
        if visited[vertex] == False:
            pathExitsUtil(graph, vertex, end_vertext, visited, path, paths)



if __name__ == '__main__':
    g = {
     1: [2, 3],
     2: [3],
     3: [] 
    }
    print(pathExits(g, 1, 3))
    print(pathExits(g, 3, 1))
