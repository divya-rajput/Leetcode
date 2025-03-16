'''
    Leetcode-129---> Sum Root to Leaf Numbers
    You are given the root of a binary tree containing digits from 0 to 9 only.
    Each root-to-leaf path in the tree represents a number.
    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
    A leaf node is a node with no children.
    Input: root = [1,2,3]
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Copy the below code in Leetcode

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(sum, root):
            if not root:
                return 0   
            sum = sum * 10 + root.val
            if not root.left and not root.right:
                return sum
            return helper(sum, root.left) + helper(sum, root.right)
        
        return helper(0, root)
        