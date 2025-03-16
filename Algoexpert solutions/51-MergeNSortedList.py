from heapq import heappush as push, heappop as pop

class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next
    def __repr__(self) -> str:
        return str(self.value)
    def __lt__(self, other):
        return self.value < other.value

class Solution:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        ans = ListNode()
        heap = list()
        
        def printNode(node):
            while node != None:
                print(node.value)
                node = node.next
        
        def insert(head: ListNode):
            if head is not None:
                push(heap, (head.value, head))
                
        for head in lists:
            insert(head)
        ans = dummy = ListNode()    
        while len(heap) > 0:
            currNode = pop(heap)    
            currList = currNode[1]
            ans.next = currList
            currList = currList.next
            ans = ans.next
            insert(currList)   
        printNode(dummy.next)
        return
    
if __name__ == "__main__":
    def arr_to_list(arr):
        i = 0
        head = cur = ListNode()
        for value in arr:
            cur.next = ListNode(value)
            cur = cur.next
        return head.next
    input = [
    [1,4,5],
    [1,3,4],
    [2,6]
    ]
    sol = Solution()
    sol.mergeKLists(list(map(arr_to_list, input)))
    # while output:
    #     print(output.value)