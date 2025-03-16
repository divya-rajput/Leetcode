
count = 0
# island_mat = [
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0]
# ]

# island_mat = [
#     [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
#     [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
#     [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
#     [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
#   ]

island_mat =[
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1]
  ]
m,n = len(island_mat[0]),len(island_mat)
visited = list(list(False for _ in range(m)) for _ in range(n))

def is_safe(r,c,island):
    global visited,m,n
    return r < n and r >= 0 and c < m and c >= 0 and island_mat[r][c] == 1 and not visited[r][c]

def island(m,n):
    ans = []
    for i in range(n):
        for j in range(m):
            result = dfs(i,j)
            print(result)
            if result != 0:
                ans.append(result)
                result = 0  
    return ans     

def dfs(r,c):
    global visited,count,island_mat
    if not is_safe(r,c,island_mat):
        return 0
    visited[r][c] = True
    return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)

print(island(m,n))