'''
Created on 09-Sep-2016

@author: anpradha

Problem : 
1 . Given a graph and a source vertex in graph, find shortest paths from source to all vertices in the given graph.
2 . Given a graph and a source vertex in graph, find shortest paths from source to end vertex


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
4. pop and element from min heap and follow the process until we visit the end vertex
'''

import heapq
def shortestPath(graph, start, end_vertex):
    
    ''' Initialized queue with start point cost is 0'''
    # its a array with each element as a tuple (cost,vertex,path[])
    
    queue = [(0, start, [])]
    
    # visited set
    '''Define a set for visited list '''
    seen = set()
    while True:
        (cost, vertex, path) = heapq.heappop(queue)
        
        if vertex not in seen:
            path = path + [vertex]
            ''' vertex is not in visited list , add it '''
            seen.add(vertex)

            '''  if vertex reached end vertex , we are done'''
            if vertex == end_vertex:
                return cost, path
            
            ''' Update the cost for all adjacent vertex '''
            for (next_vertex, cost_vertex) in graph[vertex].items():
                heapq.heappush(queue, (cost + cost_vertex, next_vertex, path))

   

if __name__ == '__main__':
    G = {'s': {'u':10, 'x':5},
        'u': {'v':1, 'x':2},
        'v': {'y':4},
        'x':{'u':3, 'v':9, 'y':2},
        'y':{'s':7, 'v':6}}


    print(shortestPath(G, 's', 'v'))

   
