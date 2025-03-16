'''
    Leetcode-590---> N-ary Tree Postorder Traversal
    Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
    Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value.
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [5,6,3,2,4,1]
'''
# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


#Copy the below code in Leetcode

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.helperPostorder(root,result)
        return result

    def helperPostorder(self,root,result):
        if root == None:
            return
        for node in root.children:
            self.helperPostorder(node,result)
        result.append(root.val)
        return result