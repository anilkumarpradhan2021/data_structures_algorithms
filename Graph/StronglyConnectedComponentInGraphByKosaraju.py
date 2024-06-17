'''
Created on 07-Oct-2016

@author: anpradha

Problem Statement:
        Implement SCCs(Strongly Connected Component) of a directed Graph , to show strongly connected components 
        in the given Graph

SCCs: All the vertices in a group of cluster from where each node is reachable from every other node.

Formal Definition: vertex 'v' and 'w' are strongly connected if there exists a directed path from 'v' to 'w' and also directed path from 'w' to 'v'.

Properties of SCCs:
1. Equivalence Relation :
         If 'v' is strongly connected to 'w', then 'w' is strongly connected to 'v'.
2. Transitive Property: 
    If  'v' is strongly connected to 'w' and 'w' is strongly connected to 'y' , then 'v' is strongly connected to 

Real Life based Application of SCCs: 
1. Probably Facebook   recommends Friends using SCC.
2. LinkedIn shows 1st or 2nd or 3rd Connection using the concept of SCC. 

Kosaraju's Algorithm:
1. Given a directed graph G , and stack S of size equal to number of vertices.
2. While S does not contain all the vertices, perform step 3.
3. Start DFS at any random vertex, Each time a DFS finishes for a vertex 'v' , push it onto the stack,
   this will fill the stack with least finishing time at the bottom and with maximum finish time closer  to top of stack. In simple words we are putting reverse post order of the graph in the stack.

4. Obtain Transpose of the given directed Graph.
          Transpose of Graph: Graph with the direction of every edge reversed.
5. While Stack S is not empty, perform step 6.
6. Pop the top element of stack and perform DFS on the transposed graph, for every item poped  from the stack and the vertices visited from poped item are strongly connected.


Note: SCC for a direct graph and its Transpose Graph(the same graph with the direction of every edge reversed) has exactly the same SCC as the original graph, because of the Transitive Property.

 Time Complexity:  O (V+E)
           The above complexity is obtained from following steps:


Check the downloaded video for better understanding

'''


def dfs(graph):
    ''' queue for tracking if vertex is visited or not'''
    visited = {v:False for v in graph.keys()}
    
    
    for vertex in graph.keys():
        if visited[vertex] == False:
            dfsUtil(graph, vertex, visited)
    

def dfsUtil(graph, vertex, visited):
    visited[vertex] = True
    
    print(vertex, end=" ")
    for v in graph[vertex]:
        if visited[v] == False:
            dfsUtil(graph, v, visited)


def fillOrder(graph, vertex, visited, stack):
    visited[vertex] = True
    
    for v in graph[vertex]:
        if visited[v] == False:
            fillOrder(graph, v, visited, stack)
    stack.append(vertex)        


def traspose_graph(graph):
    temp = {v:[] for v in graph}
    
    for v in graph:
        for u in graph[v]:
            temp[u] = temp[u] + [v] 
            
    
    return temp       
        
def print_ssc(graph):

    ''' step-1  Mark all the vertices as not visited (For first DFS) '''
    visited = {v:False for v in graph.keys()}
    
    ''' Create the stack  to Fill vertices in stack according to their finishing times'''
    stack = []
    
    for vertex in graph.keys():
        if visited[vertex] == False:
            fillOrder(graph, vertex, visited, stack)
    
    ''' Step-2 Transpose or reverse the graph '''
    g = traspose_graph(graph)
    
    ''' Mark all the vertices as not visited (For 2nd DFS) '''
    visited = {v:False for v in graph.keys()}
    
    ''' Till the stack is empty'''
    while len(stack):
        
        ''' Pop a vertex from stack'''
        vertex = stack.pop()
        
        '''Print Strongly connected component of the popped vertex '''
        if visited[vertex] == False:
            dfsUtil(g, vertex, visited)
            print()

    
if __name__ == '__main__':
    g = {
     0: [2, 3],
     1: [0],
     2: [1],
     3: [4],
     4: []
    }
    print_ssc(g)
    
    
