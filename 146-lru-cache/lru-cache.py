class LinkedNode:
    def __init__(self,key, val, prev=None,next=None):
        self.key = key 
        self.val = val 
        self.prev = prev
        self.next = next 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None 
        self.tail = None 
        self.dict = {}
    def delete(self, node):
        # delete node in linkedList 
        del self.dict[node.key]
        if node == self.head: 
            self.head = node.next 
            # self.head.prev = None 
        if node == self.tail: 
            self.tail = node.prev
            # self.tail.next = None 
        if node.prev and node.next: 
            node.next.prev = node.prev
            node.prev.next = node.next
        elif node.prev and not node.next: 
            node.prev.next = None
        elif not node.prev and node.next: 
            node.next.prev = None
        

    def get(self, key: int) -> int:
        if key not in self.dict.keys():
            return -1
        else: 
            node = self.dict[key]
            val = node.val
            self.delete(node)
            self.put(key,val)
            return val
                
    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            node = self.dict[key]
            self.delete(node)
        node = LinkedNode(key,value)
        if not self.tail: 
            self.head = node 
        else: 
            self.tail.next = node
            node.prev = self.tail 
        self.tail = node 
        self.dict[key]= node
        

        if self.cap < len(self.dict):
            self.delete(self.head)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)