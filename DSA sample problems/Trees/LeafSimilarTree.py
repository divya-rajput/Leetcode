'''
    Leetcode-872---> Leaf-Similar Trees
    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
    For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
    Two binary trees are considered leaf-similar if their leaf value sequence is the same.
    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        output1 = []
        output2 = []
        self.getLeafNode(root1,output1)
        self.getLeafNode(root2,output2)       
        return output1==output2

    def getLeafNode(self,root,result):
        if root == None:
            return
        if root.left == None and root.right == None:
            result.append(root.val)
        self.getLeafNode(root.left,result)
        self.getLeafNode(root.right,result)

        return result
        