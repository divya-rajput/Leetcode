#Complexity analysis 
#Time complexity- O(logn), Space complexity- O(1)

def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree,target,float("inf"))

def findClosestValueHelper(node,target,closest):
    if node is None:
        return closest
    if abs(target - closest) > abs(target - node.value):
        closest = node.value
    if target < node.value:
        return findClosestValueHelper(node.left,target,closest)
    elif target > node.value:
        return findClosestValueHelper(node.right,target,closest)
    else:
        return closest
    


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
