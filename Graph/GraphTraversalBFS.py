'''
Created on 02-Oct-2016

@author: anpradha


Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree
The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again.
To avoid processing a node more than once, we use a boolean visited array. 
For simplicity, it is assumed that all vertices are reachable from the starting vertex.


Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.



'''
from queue import Queue

class Graph():
    
    def __init__(self, number_of_vertices):
        self.adjacency_list = [[] for _ in range(number_of_vertices)]
        self.number_of_vertices = number_of_vertices
    
    def add_edge(self, vertex, node):
        self.adjacency_list[vertex].append(node)    
        
    def __repr__(self):
        return  str(self.adjacency_list)   

    def print_graph(self):
        for i in range(self.number_of_vertices):
            current_vertex = i
            print(current_vertex, end=' - >')
            for vertex in range(len(self.adjacency_list[current_vertex])):
                print(self.adjacency_list[current_vertex][vertex], end=' ->')
            print()    

    def bfs_util(self, q, vertix, visited):
        
        ''' Mark current vertex as visited '''
        q.put(vertix)
        visited[vertix] = True
        
                
        while not q.empty():
            current_vertex = q.get()
            print(current_vertex, end=' ')
            
            for i in range(len(self.adjacency_list[current_vertex])):
                next_vertex = self.adjacency_list[current_vertex][i]
                if visited[next_vertex] == False:
                    q.put(next_vertex)
                    ''' Now make the vertex as visited '''
                    visited[next_vertex] = True
            
                
        
    def bfs(self):
        visited = [False for _ in range(self.number_of_vertices)]

        q = Queue()
        
        for c in range(self.number_of_vertices):
            if visited[c] == False:
                self.bfs_util(q, c, visited)
                    
    def bfs2(self):
        visited = [False for _ in range(self.number_of_vertices)]

        q = Queue()
        
        for c in range(self.number_of_vertices):
            if visited[c] == False:
                for j in range(len(self.adjacency_list[c])):
                    if visited[self.adjacency_list[c][j]] == False:
                         visited[self.adjacency_list[c][j]] = True
                         #print(visited)
                         print(self.adjacency_list[c][j])

    
if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g)
    g.print_graph()
    print("Graph Traversal in BFS ")
    g.bfs()
    g.bfs2()
    
