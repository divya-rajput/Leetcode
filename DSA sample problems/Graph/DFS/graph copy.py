# your code goes here
adj = [[], [2,3,6], [1,5], [1,4], [3], [2], [1, 8], [], [6, 9, 10], [8], [8]]
visited = set()

def dfs(node, target):
	global adj
	global visited
	if node in visited:
		return False
	visited.add(node)
	# print(node, "set", visited)
	if node == target:
		return True
	for child in adj[node]:
		print(node, child)
		if dfs(child, target):
			return True
	return False
	
print(dfs(1, 5))
print(visited)