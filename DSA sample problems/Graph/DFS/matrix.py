rocks = []
n = 3
m = 4
visited = list(list(False for _ in range(m)) for _ in range(n))

rocks = [(0, 0), (1 ,1), (2, 2)]
rocks_matrix = list(list(False for _ in range(m)) for _ in range(n))
for rock in rocks:
    rocks_matrix[rock[0]][rock[1]] = True

def is_safe(r, c):
    global visited, n, m
    return r < n and r >= 0 and c < m and c >= 0 and visited[r][c] == False and rocks_matrix[r][c] == False

def dfs(r, c, tr, tc):
    global visited
    if not is_safe(r, c):
        return False
    visited[r][c] = True

    if r == tr and c == tc:
        return True
    
    if dfs(r-1, c, tr, tc):
        return True
    elif dfs(r+1, c, tr, tc):
        return True
    elif dfs(r, c-1, tr, tc):
        return True
    elif dfs(r, c+1, tr, tc):
        return True
    return False

print(dfs(0, 3, 2, 0))