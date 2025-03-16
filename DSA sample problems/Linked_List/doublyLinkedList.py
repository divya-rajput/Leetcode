class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def appendNodeOnHead(self,data):
        newNode = Node(data)
        newNode.next = self.head
        if(self.head is not None):
            self.head.prev = newNode
        self.head = newNode

    def appendNodeIntheMiddle(self,prev_node,data):
        newNode = Node(data)
        newNode.next = prev_node.next
        prev_node.next = newNode
        newNode.prev = prev_node
        newNode.next.prev = newNode


    def appendNodeAtLast(self,data):
        newNode = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        last = cur
        last.next = newNode
        newNode.prev = last
        newNode.next = None




    
    def printList(self):
        print("*****Printing the list****")
        cur = self.head
        while cur:
            print(cur.data)
            last = cur
            cur = cur.next
        print("***** Printing the list in reverse order*****")
        while last:
            print(last.data)
            last = last.prev


if __name__ == "__main__":
    llist = DoublyLinkedList()
    llist.appendNodeOnHead(1)
    llist.appendNodeOnHead(2)
    llist.appendNodeOnHead(3)
    llist.appendNodeOnHead(4)
    llist.appendNodeIntheMiddle(llist.head.next.next,5)
    llist.appendNodeAtLast(6)
    llist.printList()
