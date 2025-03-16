'''
    Leetcode-965---> Univalued Binary Tree
    A binary tree is uni-valued if every node in the tree has the same value.
    Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
    Input: root = [1,1,1,1,1,null,1]
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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        return self.isSame(root,root.val)


    def isSame(self,root,val) -> bool:
        if not root:
            return True
        if root.val != val:
            return False
        left = self.isSame(root.left,val)
        right = self.isSame(root.right,val)
        return left and right