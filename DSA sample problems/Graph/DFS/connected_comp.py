adj = [[], [2,3,6], [1,5], [1,4], [3], [2], [1, 8], [], [6, 9, 10], [8], [8]]
visited = set()
def connected_component(n,adj):
    global visited
    components = []
    for node in range(n):
        if node not in visited:
            component = dfs(node,adj,visited)
            components.append(component)
    return components

def dfs(n,adj,visited):
    if n in visited:
        return []
    visited.add(n)
    component = [n]
    for child in adj[n]:
        if child not in visited:
            c_comp = dfs(child,adj,visited)
            component.extend(c_comp)
    return component

def dfs_target(node, target):
	global adj
	global visited
	if node in visited:
		return False
	visited.add(node)
	print(node, "set", visited)
	if node == target:
		return True
	for child in adj[node]:
		print(node, child)
		if dfs_target(child, target):
			return True
	return False
print(connected_component(len(adj),adj))	
print(dfs_target(1, 5))