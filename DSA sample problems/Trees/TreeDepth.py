'''
    104. Maximum Depth of Binary Tree   
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

'''
from typing import Optional


class TreeNode:
    #Constructing a tree node- Way 1
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
    #Constructing a tree node- Way 2    
    # def __init__(self,val=0):
    #     print("Hey there!!")
    #     self.val = val
    #     self.left = None
    #     self.right = None

class TreeDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return 1+max(leftDepth,rightDepth)
    
if __name__ == "__main__":
    td = TreeDepth()
    input = [3,9,20,None,None,15,7]
    #Constructing a tree node- Way 1
    root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    #Constructing a tree node- Way 2
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.left.left = None
    # root.left.right = None
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    # root.right.left.left = None
    # root.right.left.right = None
    # root.right.right.left = None
    # root.right.right.right = None
    
    
    print("Tree-Depth: ",td.maxDepth(root))