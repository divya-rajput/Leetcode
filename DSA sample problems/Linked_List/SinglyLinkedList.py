class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    #initializing head of a linked list
    def __init__(self):
        self.head = None

    def appendBeginning(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def appendLast(self,data):
        newNode = Node(data)
        cur = self.head
        while cur.next != None:
            cur =cur.next
        cur.next = newNode
        newNode.next = None

    def appendInTheMiddle(self,prev_node,data):
        if prev_node == None:
            print("Node not found!!!Data cannot be inserted!!")
            return
        
        newNode = Node(data)
        newNode.next = prev_node.next
        prev_node.next = newNode

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next



    #Printing a linked list

if __name__ == '__main__':
    llist = SinglyLinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    #llist.printList()
    llist.appendBeginning(0)
    #.printList()
    llist.appendLast(4)
    llist.appendInTheMiddle(llist.head.next,6)
    llist.printList()