'''
Created on 02-Oct-2016

@author: anpradha



Topological Sorting

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv,
 vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

For example, a topological sorting of the following graph is “5 4 2 3 1 0″. There can be more than one topological sorting
for a graph. For example, another topological sorting of the following graph is “4 5 2 3 1 0″. 
The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no in-coming edges).

Topological Sorting vs Depth First Traversal (DFS):
In DFS, we print a vertex and then recursively call DFS for its adjacent vertices. 
In topological sorting, we need to print a vertex before its adjacent vertices. For example, in the given graph, 
the vertex ‘5’ should be printed before vertex ‘0’, but unlike DFS, the vertex ‘4’ should also be printed before vertex ‘0’.
So Topological sorting is different from DFS. For example, a DFS of the above graph is “5 2 3 1 0 4″, 
but it is not a topological sorting

Please check the downloaded video for any doubt

'''
from builtins import range


class Graph():
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.adjacency_list = [[] for _ in range(number_of_vertices)]
        
    def add_edge(self, vertex, vertex_to_add):
        self.adjacency_list[vertex].append(vertex_to_add)    
    
    def __repr__(self):
        return (str(self.adjacency_list))    

    def print_graph(self):
        for i in range(self.number_of_vertices):
            current_vertex = i
            print(current_vertex, end=' - >')
            for vertex in range(len(self.adjacency_list[current_vertex])):
                print(self.adjacency_list[current_vertex][vertex], end=' ->')
            print()    
    def topological_sort_util(self, vertex, visited, stack):
        
        ''' Mark the current node as visited '''
        visited[vertex] = True
        
        
        '''Recur for all the vertices adjacent to this
        // vertex
        '''
        for i in range(len(self.adjacency_list[vertex])):
            next_vertex = self.adjacency_list[vertex][i]
            if visited[next_vertex] == False:
                self.topological_sort_util(next_vertex, visited, stack)
        
        '''Push current vertex to stack which stores result '''        
        stack.append(vertex)        
        
        
    def topological_sort(self):
        
        '''Mark all the vertices as not visited '''
        visited = [False for _ in range(self.number_of_vertices)]
        
        stack = []
        
        '''// Call the recursive helper function to store
        // Topological Sort starting from all vertices
        // one by one
        '''
        for i in range(self.number_of_vertices):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        
        ''' Print contents of stack '''
        while len(stack) > 0:
            print(stack.pop(), end=" ")
        
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.print_graph()
    g.topological_sort()

