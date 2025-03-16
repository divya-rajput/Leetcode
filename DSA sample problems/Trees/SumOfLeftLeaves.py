'''
    Leetcode-404---> Sum of Left Leaves
    Given the root of a binary tree, return the sum of all left leaves.
    A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
    Input: root = [3,9,20,null,null,15,7]
    Output: 24
    Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Copy the below code in Leetcode

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # return self.findSum(root,False)
        return self.solve(root)
    
    def isLeaf(self, node):
        return node is not None and node.left is None and node.right is None

    def solve(self, root): 
        ans = 0
        if root.left:
            ans = root.left.val if self.isLeaf(root.left) else self.solve(root.left)
        if root.right:
            ans += self.solve(root.right)
        return ans

    def findSum(self,root,leaf) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None and leaf:
            return root.val
        left = self.findSum(root.left,True)
        right = self.findSum(root.right,False)
        return left+right