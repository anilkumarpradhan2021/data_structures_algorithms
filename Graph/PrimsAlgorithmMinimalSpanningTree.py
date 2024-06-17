'''
Created on 04-Oct-2016

@author: anpradha

Problem :
1 . We want to find a minimum spanning tree for a connected weighted undirected graph. 

Steps 
1. Create visited and a min heap
2. Add start vertex to min heap with cost as 0
3. pop element and check 
if it is not visited , 
 3.1 then visit all adjacency vertex 
 3.2 update the cost for all adjacent vertex and 
 3.3 add all adjacent to min heap.
 
else:
    do nothing
    
4. pop and element from min heap and follow the process untill we visit the end vertex
'''

import heapq
def shortestPath(graph, start):
    
    ''' Initialized queue with start point cost is 0'''
    # its a array with each element as a tuple (cost,vertex,path[])
    
    # cost, start_vertex , parent   
    queue = [(0, start, -1)]
    parent = []
    
    # visited set
    '''Define a set for visited list '''
    seen = set()
    while True:
        ''' each time it will return the vertex with minimum cost '''
        (cost, vertex, parent_vertex) = heapq.heappop(queue)
            
        if vertex not in seen:
            ''' vertex is not in visited list , add it '''
            seen.add(vertex)
            parent.append((vertex, parent_vertex))
            if len(seen) == len(graph):
                break
            
            ''' Update min heap with  all adjacent vertex cost,vertex,parent '''
            for (next_vertex, cost_vertex) in graph[vertex].items():
                heapq.heappush(queue, (cost_vertex, next_vertex, vertex))
    return parent            
        

if __name__ == '__main__':
    G = {'s': {'u':10, 'x':5},
        'u': {'v':1, 'x':2},
        'v': {'y':4},
        'x':{'u':3, 'v':9, 'y':2},
        'y':{'s':7, 'v':6}}

    print(shortestPath(G, 's'))
    print("length :" + str(len(G)))

   
