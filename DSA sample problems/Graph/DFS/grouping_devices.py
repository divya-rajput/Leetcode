import sys
sys.setrecursionlimit(1000_000_000)

import json
visited = set()
result = []
def printAllMembers(graph,node,visited):
    if node not in visited:
        visited.add(node)
        result.extend(graph[node]['members'])
        for neighbour in graph[node]['group']:
            printAllMembers(graph,neighbour,visited)
    return result
    
groups = """{
		"g1": {
        "group" : ["g3","g5"],
        "members" : ["Device-101","Device-107"]
        },
        "g2": {
        "group" : ["g5"],
        "members" : ["Device-102","Device-106"]
        },
        "g3": {
        "group" : ["g4"],
        "members" : ["Device-103","Device-107"]
        },
        "g4": {
        "group" : ["g5"],
        "members" : ["Device-104","Device-108"]
        },
        "g5": {
        "group" : [],
        "members" : ["Device-105","Device-109"]
        }}
        """
graph = json.loads(groups)
print("Device list are = ",printAllMembers(graph,"g1",visited))
