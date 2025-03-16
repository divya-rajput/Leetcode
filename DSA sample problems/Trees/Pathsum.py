'''
Lettcode-112---> Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Copy the below code in Leetcode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.findTargetSum(root,targetSum,0)

    def findTargetSum(self,root,targetSum,currSum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            # currSum += root.val
            return  (currSum+root.val) == targetSum

        return self.findTargetSum(root.left,targetSum,currSum+root.val) or self.findTargetSum(root.right,targetSum,currSum+root.val)

