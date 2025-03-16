'''
    Leetcode-257---> Binary Tree Paths
    Given the root of a binary tree, return all root-to-leaf paths in any order.
    A leaf is a node with no children.
    Input: root = [1,2,3,null,5]
    Output: ["1->2->5","1->3"]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Copy the below code in Leetcode

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result =[]
        self.pathFinder(root,result,"")
        return result

    def pathFinder(self,root,result,currentPath):
        if root == None:
            return
        if root.left == None and root.right == None:
            currentPath += str(root.val)
            result.append(currentPath)
        
        currentPath += str(root.val) + "->"
        self.pathFinder(root.left,result,currentPath)
        self.pathFinder(root.right,result,currentPath)

