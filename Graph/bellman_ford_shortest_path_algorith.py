'''
Created on 03-Oct-2016

@author: anpradha

Problem : 
1 . Given a graph and a source vertex in graph, find shortest paths from source to all vertices in the given graph.


Algorithm
Following are the detailed steps.

Input: Graph and a source vertex src
Output: Shortest distance to all vertices from src. If there is a negative weight cycle, then shortest distances are not 
calculated, negative weight cycle is reported.

1) This step initializes distances from source to all vertices as infinite and distance to source itself as 0. 
Create an array dist[] of size |V| with all values as infinite except dist[src] where src is source vertex.

2) This step calculates shortest distances. Do following |V|-1 times where |V| is the number of vertices in given graph.
…..a) Do following for each edge u-v
………………If dist[v] > dist[u] + weight of edge uv, then update dist[v]
………………….dist[v] = dist[u] + weight of edge uv

3) This step reports if there is a negative weight cycle in graph. Do following for each edge u-v
……If dist[v] > dist[u] + weight of edge uv, then “Graph contains negative weight cycle”
The idea of step 3 is, step 2 guarantees shortest distances if graph doesn’t contain negative weight cycle. If we iterate through all edges one more time and get a shorter path for any vertex, then there is a negative weight cycle


Complexity : O(VE)
'''

import heapq
import sys
def shortestPath(graph, start):
    
    ''' Step 1: Initialize distances from src to all other vertices as INFINITE'''
    
    distance = {v:sys.maxsize for v in graph.keys()}
    distance[start] = 0
    print(distance)
    print(len(distance))
    
    '''Step 2: Relax all edges |V| - 1 times. A simple shortest path from src to any other vertex can have at-most |V| - 1 edges'''
    for i in range(1, len(distance)):
        for u in graph:  #  for each vertex
            for v in graph[u]:  # For each neighbour/adjacency list  of u
                print("distance[v] : " + str(distance[v]))
                print("distance[u] : " + str(distance[u]))
                print("graph[u][v] : " + str(graph[u][v]))
                
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]
    
    ''' Step 3: check for negative-weight cycles.  The above step guarantees shortest distances if graph doesn't
        contain negative weight cycle. If we get a shorter even after above steps ,then there is a cycle.'''                
    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            # this shd be always distance[v] <= distance[u] + graph[u][v] for non negative weight cycle 
            assert distance[v] <= distance[u] + graph[u][v]
    
    print(distance)        

            

if __name__ == '__main__':
    G = {
        'a': {'b':-1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d':-3}
        }

    print(shortestPath(G, 'a'))
