from heapq import heappush as push, heappop as pop
class Solution:
    def solve(self,x, start):
        n = len(x)
        visited = [False]*n
        cost = [float('inf')]*n
        h = []
        cost[start] = 0
        h.append([0,start])
        while len(h) > 0:
            curr_Weight, curr_node = pop(h)
            print(curr_Weight,curr_node)
            if visited[curr_node] is True:
                continue
            visited[curr_node] = True
            
            for child in x[curr_node]:
                child_node, child_weight = child
                cost[child_node] = min(cost[child_node],curr_Weight+child_weight)
                if not visited[child_node]:
                    push(h,[cost[child_node],child_node])
                    
        print(cost)
    
solution = Solution()

import sys

f = open("input.txt", "r")
sys.stdin = f
n, e = map(int, input().split())
x = [[] for _ in range(n+1)]
for _ in range(e):
    v1, v2, wt = map(int, input().split())
    x[v1].append([v2, wt])
    x[v2].append([v1, wt])
start = int(input())
f.close()
solution.solve(x, start)