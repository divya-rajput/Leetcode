# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traversal(node, curr_sum):
            if node == None:
                return False
            curr_sum += node.val
            if node.left == None and node.right== None:
                return curr_sum == targetSum
            return traversal(node.left,curr_sum) or traversal(node.right,curr_sum)
        return traversal(root,0)