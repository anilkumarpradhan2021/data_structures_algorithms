'''
Created on 06-Oct-2016

@author: anpradha



The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. 
The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.

Example:

Input:
       graph[][] = { {0,   5,  INF, 10},
                    {INF,  0,  3,  INF},
                    {INF, INF, 0,   1},
                    {INF, INF, INF, 0} }
which represents the following graph
             10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3       
Note that the value of graph[i][j] is 0 if i is equal to j 
And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.

Output:
Shortest distance matrix
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0 

Steps
1. Create distance and path matrix as above (2 dimentional) 
2.1for distance 
    if vertex are not connected then 
        put INF 
    else 
        put the weight between them
2.2 For path 
    if exists from v1 to v2 then 
        put v1 
    else 
        put -1
2.3 for all diagonal in distance put 0 i.e distance[i][i] = 0
3. Three for loop and find and update the distance/path as below
    if distance [i][j]  > distance[i][k] + distance[k][j] then 
        distance [i][j] = distance[i][k] + distance[k][j]
        path[i][j] = path[k][j]
    else:
        do nothing



Complexity : O(V3)        
'''
def floydWarshall(graph):
    
    distacne = {}
    path = {}
    for u in graph:
        distacne[u] = {}
        path[u] = {}
        for v in graph:
            distacne[u][v] = float("inf")
            path[u][v] = -1
        distacne[u][u] = 0
        for neighbour in graph[u]:
            distacne[u][neighbour] = neighbour
            path[u][neighbour] = u        
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if distacne[i][j] > distacne[i][k] + distacne[k][j]:
                    distacne[i][j] = distacne[i][k] + distacne[k][j]
                    path[i][j] = path[k][j]
       
    
    print("shortest distance of each vertex to other vertex:")
    print_it(distacne)
    print("path of each vertex to other vertex")
    print_it(path)
    
    print("Testing for path from 1 to 5")
    print_path(1, 5, path)

def print_it(it):
    for i in range(len(it)):
        print(i , end="- ")
        for j in range(len(it)):
            print(it[i][j], end=' ')
        print()

def print_path(start_vetex, end_vertex, path):
    vertex_path = [end_vertex]
    temp = path[start_vetex][end_vertex]
        
    while True:
        vertex_path = vertex_path + [temp]
        if temp == start_vetex:
            break
        temp = path[start_vetex][temp]
    print(vertex_path[::-1])    
                
if __name__ == '__main__':
    graph = {0 : {1:6, 2:8},
         1 : {4:11},
         2 : {3: 9},
         3 : {},
         4 : {5:3},
         5 : {2: 7, 3:4}}
    
    floydWarshall(graph)
