count = 0
counter_dict = dict()
deps = [
  [1, 2],
  [1, 3],
  [3, 2],
  [4, 2],
  [4, 3]
]

def isTopologicalSortOrder(deps):
    for i in range(len(deps)):
        if counter_dict[deps[i][0]] < counter_dict[deps[i][1]]:
            return True
        else:
            False
def topoSort(): 
    global deps    
    adj = [[],[],[1,3,4],[1,4],[]]
    visited = set()
    stack = []
    
    count = 0
    for i in range(len(adj)):
        dfs(i,visited,stack,adj)
    if isTopologicalSortOrder(deps):
        return stack 
    

def dfs(node,visited,stack,adj):
    global count, counter_dict
    if node in visited:
        return 
    if node != 0:
        visited.add(node)
    for child in adj[node]:
        if child != 0:
            dfs(child,visited,stack,adj)
    if node != 0:
        count += 1
        counter_dict[node] = count
        stack.append(node)       
    return stack
print(topoSort())

