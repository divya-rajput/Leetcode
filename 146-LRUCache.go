
// Actual cache data structure
type LRUCache struct {
    TotalCapacity int
    CurrentCapacity int
    Head *DoublyLinkedList
    Tail *DoublyLinkedList
    Cache map[int]*DoublyLinkedList
}

// To maintain the order of usage
type DoublyLinkedList struct {
    prev *DoublyLinkedList
    next *DoublyLinkedList
    key     int
    val     int
}

// Least recently used is always added next to Head node.
func (this *LRUCache) addNode(node *DoublyLinkedList){
    node.prev = this.Head
    node.next = this.Head.next
    this.Head.next.prev = node
    this.Head.next = node
}

// Remove the node from the DLL
func (this *LRUCache) removeNode(node *DoublyLinkedList){
    node.prev.next = node.next
    node.next.prev = node.prev
    node.next =  nil
    node.prev = nil
}

// Last accessed is moved to the front of the queue as most recently used
func (this *LRUCache) addToFront(node *DoublyLinkedList){
    this.removeNode(node)
    this.addNode(node)
}

// Init the map, cap & marker nodes for Head & Tail
func Constructor(capacity int) LRUCache {
    obj := LRUCache{
        TotalCapacity: capacity,
        Cache: make(map[int]*DoublyLinkedList),
    }
    obj.Head = &DoublyLinkedList{}
    obj.Tail = &DoublyLinkedList{}
    obj.Head.next = obj.Tail
    obj.Tail.prev = obj.Head
    return obj
}

// Access it from the Map amd elevate it as MRU
func (this *LRUCache) Get(key int) int {
    if node,ok := this.Cache[key];ok{
        this.addToFront(node)
        return node.val
    }else{
        return -1
    }
}

// If already found, update the value, else
// Add it newly if we have capacity, if not,
// remove the LRU node which is previous to our tail
func (this *LRUCache) Put(key int, value int)  {
    if node,ok := this.Cache[key];ok{
        node.val = value
        this.addToFront(node)
    }else{
        if this.CurrentCapacity < this.TotalCapacity {
            node := &DoublyLinkedList{
                key: key,
                val: value,
            }
            this.Cache[key] = node
            this.addNode(node)
            this.CurrentCapacity++
        }else{
            node := &DoublyLinkedList{
                key: key,
                val: value,
            }
            this.Cache[key] = node
            delete(this.Cache,this.Tail.prev.key)
            this.removeNode(this.Tail.prev)
            this.addNode(node)
        }
        
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */