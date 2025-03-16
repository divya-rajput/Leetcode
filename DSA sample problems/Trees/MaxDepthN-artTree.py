'''
    Leetcode-559---> Maximum Depth of N-ary Tree
    Given a n-ary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.
    Input: root = [1,null,3,2,4,null,5,6]
    Output: 3
'''
# class Node:
#     def __init__(self,value=None,children=None):
#         self.val = value
#         self.children = children

#Copy the below code in Leetcode
         
class Solution:
    def maxDepth(self,root: 'Node') -> int:
        if root == None:
            return 0
        #We need to check all the children of the root
        depth = 0
        for node in root.children:
            print("Node=",node.val)
            childrenDepth = self.maxDepth(node)
            depth = max(depth,childrenDepth)
        return depth + 1
    