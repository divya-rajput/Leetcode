'''
    Leetcode-993---> Cousins in Binary Tree
    Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
    Two nodes of a binary tree are cousins if they have the same depth with different parents.
    Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Copy the below code in Leetcode

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        level = [-1,-1]
        parent = [-1,-1]
        parentNode = TreeNode(-1)
        self.findNodes(root,x,y,parent,level,0,parentNode)
        if level[0] == level[1] and parent[0] != parent[1]:
            return True
        print(level)
        print(parent)
        return False

    def findNodes(self,root,x,y,parent,level,currLevel,currParent):
        if root == None:
            return 
        if root.val == x:
            level[0] = currLevel
            parent[0] = currParent.val
        if root.val == y:
            level[1] = currLevel
            parent[1] = currParent.val
        self.findNodes(root.left,x,y,parent,level,currLevel+1,root)
        self.findNodes(root.right,x,y,parent,level,currLevel+1,root)