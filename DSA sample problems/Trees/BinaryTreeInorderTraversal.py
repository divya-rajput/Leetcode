'''
    Leetcode-94. Binary Tree Inorder Traversal
    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    Input: root = [1,null,2,3]
    Output: [1,3,2]
    
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Copy the below code in Leetcode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helperInorderTraversal(root,result)
        return result

    def helperInorderTraversal(self,root,result) -> List[int]:
        if root == None:
            return
        self.helperInorderTraversal(root.left,result)
        result.append(root.val)
        self.helperInorderTraversal(root.right,result)
        return result