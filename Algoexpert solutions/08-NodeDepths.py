#Complexity analysis 
#Time complexity- O(n), Space complexity- O(h)
sum_depth = 0
def nodeDepths(root):
    global sum_depth 
    sum_depth = 0
    sumOfNodeDepth(root,0)
    return sum_depth
    pass
def sumOfNodeDepth(Node,depth):
    global sum_depth
    if Node == None:
        return
    sum_depth += depth
    sumOfNodeDepth(Node.left,depth+1)
    sumOfNodeDepth(Node.right,depth+1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None