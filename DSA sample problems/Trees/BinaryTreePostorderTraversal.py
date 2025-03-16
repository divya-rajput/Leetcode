'''
    Leetcode-145--> Binary Tree Postorder Traversal
    Given the root of a binary tree, return the postorder traversal of its nodes' values.
    Input: root = [1,null,2,3]
    Output: [3,2,1]
    
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Copy the below code in Leetcode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helperPostorderTraversal(root,result)
        return result

    def helperPostorderTraversal(self,root,result) -> List[int]:
        if root == None:
            return
        self.helperPostorderTraversal(root.left,result)
        self.helperPostorderTraversal(root.right,result)
        result.append(root.val)
        return result