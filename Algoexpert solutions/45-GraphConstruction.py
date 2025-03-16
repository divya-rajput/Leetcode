
from collections import defaultdict

def addEdge(graph,u,v):
    graph[u].append(v)

def generateEdge(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append([neighbour])
    return edges

graph = defaultdict(list)
addEdge(graph,'a','c') 
addEdge(graph,'b','c') 
addEdge(graph,'b','e') 
addEdge(graph,'c','d') 
addEdge(graph,'c','e') 
addEdge(graph,'c','a') 
addEdge(graph,'c','b') 
addEdge(graph,'e','b') 
addEdge(graph,'d','c') 
addEdge(graph,'e','c') 
print(generateEdge(graph))
print(graph)