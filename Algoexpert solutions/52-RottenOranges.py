from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        q = deque()
        t= 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    q.append([i,j,t])         
        while len(q) > 0:
            r,c,t = q.popleft()
            visited[r][c] = True
            if self.isSafe(r-1,c,rows,columns,visited,grid):
                grid[r-1][c] = 2
                q.append([r-1,c,t+1])
            if self.isSafe(r+1,c,rows,columns,visited,grid):
                grid[r+1][c] = 2
                q.append([r+1,c,t+1])
            if self.isSafe(r,c-1,rows,columns,visited,grid):
                grid[r][c-1] = 2
                q.append([r,c-1,t+1])
            if self.isSafe(r,c+1,rows,columns,visited,grid):
                grid[r][c+1] = 2
                q.append([r,c+1,t+1])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return -1
        return t
    def isSafe(self,r,c,rows,columns,visited,grid):
            return True if(r >= 0 and r < rows) and  (c >= 0 and c < columns) and (grid[r][c] == 1) and visited[r][c] == False else False
if __name__ == "__main__":
    obj = Solution()
    grid = [[0,2]]
    grid1 = [[2,1,1],[0,1,1],[1,0,1]]
    grid2 = [[2,1,1],[1,1,0],[0,1,1]]
    grid4 = [[0]]
    grid3 = [[1]]
    print(obj.orangesRotting(grid))
    print(obj.orangesRotting(grid1))
    print(obj.orangesRotting(grid2))
    print(obj.orangesRotting(grid4))
    print(obj.orangesRotting(grid3))