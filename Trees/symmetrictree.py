# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return 
        return self.checkSym(root.left,root.right)
    
    def checkSym(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return ((left.val == right.val) and self.checkSym(left.right,right.left) and self.checkSym(left.left,right.right))