'''
    This is a Least Recently Used(LRU) problem.
    Definition:     An LRU cache is an efficient cache data structure that can be used to figure out what we should evict when the cache is full. 
                    The goal is to always have the least-recently used item accessible in O(1) time. 
    Task :          LRU will help you to quickly identify which item hasn't been used for longest amount if time.
    Implementation: LRU is often implemented by pairing a doubly link list with a hash map
    Strength:       1. Super fast access with O(1) time
                    2. Super fast update with O(1) time
    Weaknesses:     Space heavy-Contains alinked list with n length and a hash map holting n items.So, O(n) space
'''
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self,key: int) -> int:
        #If key found dictionary then first remove it and then add it at last.
        if key in self.dict:
            n = self.dict[key]
            self.remove(n)
            self.add(n)
            return n.value
        return -1
    
    def remove(self, node):
        #Using doubly link list concept pointing node previous and next to each other
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def add(self,node):
        #adding the node to the last in the linked list
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
        
    def put(self,key:int , value:int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        n = Node(key,value)
        self.add(n)
        self.dict[key] = n
        # when the len of dictionary is greater than capacity of Cache
        if len(self.dict) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dict[n.key]
        

if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    output = []
    obj = LRUCache(5)
    output.append(obj.put(1,1))
    output.append(obj.put(2,2))
    output.append(obj.put(3,3))
    output.append(obj.put(4,4))
    output.append(obj.put(5,5))
    print(obj.get(3))
    output.append(obj.put(5,3))
    print(output)
    print(obj.get(1))
    print(obj.get(2))
    print(obj.get(3))
    print(obj.get(4))
    print(obj.get(5))