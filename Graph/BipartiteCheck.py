'''
Created on 09-Oct-2016

@author: anpradha

Problem :
Check whether a given graph is Bipartite or not
A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) 
either connects a vertex from U to V or a vertex from V to U. In other words, for every edge (u, v), 
either u belongs to U and v to V, or u belongs to V and v to U. 
We can also say that there is no edge that connects vertices of same set.



Algorithm to check if a graph is Bipartite:
One approach is to check whether the graph is 2-colorable or not using backtracking algorithm m coloring problem.
Following is a simple algorithm to find out whether a given graph is Birpartite or not using Breadth First Search (BFS).
1.    Assign RED color to the source vertex (putting into set U).
2.    Color all the neighbors with BLUE color (putting into set V).
3.    Color all neighbor’s neighbor with RED color (putting into set U).
4.    This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot
 be colored with 2 vertices (or graph is not Bipartite)

Complexity : O(V+E).
'''

from queue import Queue

def checkBipartite(graph):
    
    print("graph : " + str(graph))
    
    ''' Create a color array to store colors assigned to all veritces , initially all are None'''
    colour = {v:None for v in graph}

    ''' Choose any vertex as starting point , here i have choose 1st vertex '''
    start = list(graph.keys())[0]
    
    '''Assign first color to source '''
    colour[start] = "RED"
   
    '''Create a queue for BFS traversal'''
    q = Queue()
    q.put(start)
    
 
    while not q.empty():
        
        ''' Dequeue a vertex from queue '''
        vertex = q.get()
        
        '''Find all non-colored adjacent vertices '''
        for adj_ver in graph[vertex]:
            
            '''An edge from adj_ver to graph[vertex] exists and destination adj_ver is not colored '''
            if colour[adj_ver] == None:
                
                ''' if vertex color is RED then adj_vertex (neighbours) will be BLUE or vice-versa'''
                if colour[vertex] == "RED":
                    colour[adj_ver] = "BLUE"
                else:
                    colour[adj_ver] = "RED"  
                    
                q.put(adj_ver)      
            else:
                '''An edge from adj_ver to graph[vertex] exists and destination adj_ver is same colored as graph[vertex] '''
                if colour[adj_ver] == colour[vertex]:
                    print("Its not a Bipartite")
                    return False
    
    '''If we reach here, then all adjacent vertices can be colored with  alternate color'''
    return True        

if __name__ == '__main__':
    graph = {
             1:{2, 4},
             2:{1, 3},
             3:{2, 4},
             4:{1, 3}
             }
    
    print(checkBipartite(graph))

    graph1 = {
             1:{2, 3},
             2:{1, 3},
             3:{1, 2}
             }
    
    print(checkBipartite(graph1))
