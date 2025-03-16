# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        def traversal(node):
            if node == None:
                return 
            traversal(node.left)
            ans.append(node.val)
            traversal(node.right)       
        traversal(root)
        return ans