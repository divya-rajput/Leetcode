'''
    Leetcode-101---> Symmetric Tree
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    Input: root = [1,2,2,3,4,4,3]
    Output: true
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Copy the below code in Leetcode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.findIsSymmetric(root.left,root.right)

    def findIsSymmetric(self, l,r):
        if l == None and r== None:
            return True
        elif l == None or r == None:
            return False
        elif l.val != r.val:
            return False

        self.findIsSymmetric(l.left,r.right)
        self.findIsSymmetric(l.right,r.left)