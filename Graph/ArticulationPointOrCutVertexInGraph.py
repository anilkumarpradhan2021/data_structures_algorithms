'''
Created on 08-Oct-2016

@author: anpradha

Problem :  
1 . Find the articulation point in a undirected graph 
2. Find the bridge in a graph

ARTICULATION POINT :
A vertex in an undirected connected graph is an articulation point (or cut vertex) 
iff removing it (and edges through it) disconnects the graph. Articulation points represent vulnerabilities 
in a connected network – single points whose failure would split the network into 2 or more disconnected components. 
They are useful for designing reliable networks.


BRIDGE :
An edge in an undirected connected graph is a bridge iff removing it disconnects the graph.
For a disconnected undirected graph, definition is similar, a bridge is an edge removing which increases number 
of connected components.


In DFS tree, a vertex u is articulation point if one of the following two conditions is true.
1) u is root of DFS tree and it has at least two independent children.
2) u is not root of DFS tree and it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u. 
    i.e discovery time <= low time of adjacent vertex
    discovery_time[u] <= low_time[v]
   
   
1 .Start from any vertex and do DFS  
2. For each vertex increase 
    2.2 Discovery time 
    2.3 Low time
    2.3 update adjacent vertex with updated time.
3 . Call DFS for all adjacent vertex
    3.1 each time update the low time if adjacent vertex have low time
    3.2  check for Case -1 if it is root and number of individual children > 1
    3.3  Case-2 Its not root and discovery_time of vertex is less than and equal to low time of adjacent vertex i.e  discovery_time[u] <= low_time[adj_v] 
4. Continue step-2 to 3 for all vertex     
    
    
    Please check the downloaded video for better understanding
    
'''

time = 0


def articulationPoint(graph):
    print("Graph is :" + str(graph))
    ''' mark discovery time and low time as 0 for all vertex'''
    discovery_time = {v:0 for v in graph }  # Stores discovery times of visited vertices
    low_time = {v:0 for v in graph}
    '''Mark all the vertices parent as None , Stores parent vertices in DFS tree'''
    parent = {v:None for v in graph}
    '''Mark all the vertices as not visited'''
    visited = {v:False for v in graph}
    
    
    
    '''Call the recursive helper function to find articulation'''
    for v in graph:
        if visited[v] == False:
            articulationPointUtil(graph, discovery_time, low_time, visited, v, parent)

def articulationPointUtil(graph, discovery_time, low_time, visited, u, parent):
    global time
    time = time + 1 
    childreen = 0
    visited[u] = True  # make it visited
    discovery_time[u] = time  # update discovery time
    low_time[u] = time  # update low_time
    
    for adj_v in graph[u]:
        
        ''' make current vertex as visited ''' 
        if visited[adj_v] == False:
            childreen = childreen + 1  # update child 
            parent[adj_v] = u  # update its parent
            articulationPointUtil(graph, discovery_time, low_time, visited, adj_v, parent)
            
            ''' each time update the low time if adjacent vertex have low time '''
            low_time[u] = min(low_time[u], low_time[adj_v])
            
            ''' Case -1 if it is root and number of individual children > 1'''
            if parent[u] == None and childreen > 1:
                print("Root is a Articulation point ")
                print(u)
                print("Bridge : " + str(adj_v), " " + str(u))
            
            ''' Case-2 Its not root and discovery_time of vertex is less than and equal to low time of adjacent vertex i.e  discovery_time[u] <= low_time[adj_v] '''
            if parent[u] != None and discovery_time[u] <= low_time[adj_v]:
                print("******* its a Articulation point  ******")
                print(u)
                print("Bridge : " + str(adj_v), " " + str(u))

                
        # if parent[current_vertex] == v then do nothing         
        elif adj_v != parent[u]:
            ''' condition is already visited the adjacent vertex and adjacent vertex is not the parent'''
            low_time[u] = min(low_time[u], low_time[adj_v])    
            
    
if __name__ == '__main__':  
    g = {
     0: [1],
     1: [0, 2],
     2: [1]
    }
    print(articulationPoint(g))
    g1 = {
     0: [1, 3],
     1: [0, 2],
     2: [0, 1],
     3: [0, 4],
     4: [3]
    }
    print(articulationPoint(g1))
