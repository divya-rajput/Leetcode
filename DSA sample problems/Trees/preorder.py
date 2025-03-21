# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversal(node):
            if node == None:
                return 
            ans.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return ans