'''
Created on 01-Oct-2016

@author: anpradha

Depth First Traversal for a Graph (Just print all the vertex of a graph)


Following two are the most commonly used representations of graph.
1. Adjacency Matrix
2. Adjacency List (I am using this )

list [0] connected to  {1,2} 
list [1] connected to  {2}
list [2] connected to  {0,3}
list [3] connected to  {3}


Complexity O(V+E)
V = Number of vertex
E = Number of Edge

'''

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
                

    def dfs_util(self, vertix, visited):
        
        ''' Mark current vertex as visited '''
        visited[vertix] = True
        print(vertix, end=' ')
        
        for i in range(len(self.adjacency_list[vertix])):
            next_vertex = self.adjacency_list[vertix][i]
            
            ''' 
            Recur for all the vertices adjacent to this vertex
            if next vertex is not visited then call dfs_util 
            '''
            if visited[next_vertex] == False:
                self.dfs_util(next_vertex, visited)
        
    def dfs(self):
        visited = [False for _ in range(self.number_of_vertices)]
        
        
        ''' Call the recursive helper function to print DFS traversal starting from all vertices one by one
            This is required if graph is disconnected  else not required
        '''
        for i in range(self.number_of_vertices):
            if visited[i] == False:
                self.dfs_util(i, visited)
    

    
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
    print("Graph Traversal in DFS ")
    g.dfs()
    
