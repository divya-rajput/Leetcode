matrix = [
    [1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0]
  ]

print("Input=",matrix)

rows = len(matrix)
cols = len(matrix[0])
# result_matrix = list(list(0 for _ in range(rows)) for _ in range(cols))
visited = list(list(0 for _ in range(cols)) for _ in range(rows))
print("Initial visited",visited)

def is_safe(row,col,matrix):
    global visited,rows,cols
    return row < rows and row >= 0 and col < cols and col >= 0 and matrix[row][col] == 1 and visited[row][col] == 0

def removeIsland(rows,cols,matrix,visited):
    ans = []
    j = 0
    while j < cols:
        dfs(0,j,matrix,visited)
        dfs(rows-1,j,matrix,visited)
        j += 1
    i = 0
    while i <rows:
        dfs(i,0,matrix,visited)
        dfs(i,cols-1,matrix,visited)
        i += 1
    return visited   

def dfs(r,c,matrix,visited):
    if not is_safe(r,c,matrix):
        return
    visited[r][c] = 1
    dfs(r-1,c,matrix,visited)
    dfs(r+1,c,matrix,visited)
    dfs(r,c-1,matrix,visited)
    dfs(r,c+1,matrix,visited)

print("Output=",removeIsland(rows,cols,matrix,visited))