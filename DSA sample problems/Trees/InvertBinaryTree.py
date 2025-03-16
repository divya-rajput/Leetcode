'''
    Leetcode-226---> Invert Binary Tree
    Given the root of a binary tree, invert the tree, and return its root.
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Copy the below code in Leetcode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        leftSubTree = self.invertTree(root.right)
        rightSubTree = self.invertTree(root.left)
        root.left = leftSubTree
        root.right = rightSubTree
        return root