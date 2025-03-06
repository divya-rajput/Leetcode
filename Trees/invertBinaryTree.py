# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: 
            return root
        leftSubTree = self.invertTree(root.right)
        rightSubTree = self.invertTree(root.left)
        root.left = leftSubTree
        root.right = rightSubTree
        return root
        