# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    queue = []
    def BFSTree(self, root: [TreeNode]) -> int:
        global queue
        if root is None:
            return
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                
    def BFSGraph(self,root:[TreeNode], graph) -> int:
        visited = set() 
        q = []
        if root in None:
            return
        q.append(root)
        while len(q) > 0:
            last = q.pop()
            if last not in visited:
                visited.add(last)
            for child in graph[last]:
                self.BFSGraph(child)
                
    def DFSGraph(self,root:[TreeNode], graph) -> int:
        visited = set() 
        q = []
        if root in None:
            return
        if root not in visited:
            visited.add(root)
        for child in graph[root]:
            self.DFSGraph(child)
            
            
            
        
        