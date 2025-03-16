'''
    Leetcode-144---> Binary Tree Preorder Traversal
    Given the root of a binary tree, return the preorder traversal of its nodes' values.
    Input: root = [1,null,2,3]
    Output: [1,2,3]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Copy the below code in Leetcode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helperPreorderTraversal(root,result)
        return result

    def helperPreorderTraversal(self,root,result):
        if root == None:
            return
        result.append(root.val)
        self.helperPreorderTraversal(root.left,result)
        self.helperPreorderTraversal(root.right,result)
        return result