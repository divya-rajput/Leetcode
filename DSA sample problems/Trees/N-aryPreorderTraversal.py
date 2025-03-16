'''
    Leetcode-589. N-ary Tree Preorder Traversal
    Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
    Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,3,5,6,2,4]
'''

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


#Copy the below code in Leetcode

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.helperPreorder(root,result)
        return result

    def helperPreorder(self,root,result):
        if root == None:
            return
        result.append(root.val)
        for node in root.children:
            self.helperPreorder(node,result)
        return result

