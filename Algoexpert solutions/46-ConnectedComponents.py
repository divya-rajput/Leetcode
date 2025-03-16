import sys
class Solution:
    def solve(self,x):
        count = 0
        visited = [False]*len(x)
        components = []
        print(x)
        for i in range(1, len(x)):
            start_node = i
            component = []
            self.dfs(x,start_node,visited,component)
            if len(component) > 0:
                components.append(component)
        print(components)
       
    def dfs(self,x,node,visited,component):
        if visited[node] is True: 
            return
        visited[node] = True
        component.append(node)
        for child in x[node]:
            self.dfs(x,child,visited,component)
            
        
        
solution = Solution()
try:
    f = open("input.txt", "r")
except Exception as e:
    print("Error while reading file \"input.txt\"")
sys.stdin = f
n, e = map(int, input().split())
x = [[] for _ in range(n+1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    x[v1].append(v2)
    x[v2].append(v1)
# start = int(input())
f.close()
solution.solve(x)
            