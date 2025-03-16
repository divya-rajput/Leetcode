#Complexity analysis 
#Time complexity- O(n), Space complexity- O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    node = linkedList
    count = 0
    while node != None:
        count += 1
        node = node.next
    middleNode = linkedList
    for _ in range(count//2):
        middleNode = middleNode.next
    return middleNode
