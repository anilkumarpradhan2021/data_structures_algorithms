'''
Created on 01-Oct-2019

@author: anpradha
'''


def findPathBBetweenNodes(g, startVertex, endVertex):
    visited = {vertex:False for vertex in g}
    
    # final path if any
    paths = []
    
    if visited[startVertex] == False:
        dfsUtil(g, startVertex, endVertex, visited, [], paths)

    
    print(paths)

def dfsUtil(g, startVertex, endVertex, visited, path, paths):
    
    visited[startVertex] = True
    path = path + [startVertex]
    
    for vertex in g[startVertex]:
        if vertex == endVertex:
            path = path + [endVertex    ]
            paths.append(path)
        
        if visited[vertex] == False:
            dfsUtil(g, vertex, endVertex, visited, path, paths)    


if __name__ == '__main__':
    g = {
            1: [2, 3],
            2: [3],
            3: []
        }

    findPathBBetweenNodes(g, 1, 3)
    