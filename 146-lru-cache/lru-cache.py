class LRUCache:
    class LinkNode:
        def __init__(self,key=0,val=0, prev=None, next=None):
            self.key = key 
            self.val = val 
            self.prev = prev 
            self.next = next 

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.dict = dict()
        self.head = None
        self.tail = None
  
    def addNode(self, key, value):
        node = self.LinkNode(key, value)
        if not self.head: 
            self.head = node 
            self.tail = node 
        else: 
            self.tail.next = node 
            node.prev = self.tail 
            self.tail = node 
        self.dict[key] = node 

    def deleteNode(self, key):
        node = self.dict[key]
        if node == self.head:
            self.head = self.head.next 
        if node == self.tail: 
            self.tail = self.tail.prev
        
        if node.prev: 
            node.prev.next = node.next
        if node.next: 
            node.next.prev = node.prev
        del self.dict[key]
        
    def popNode(self):
        node = self.head 
        if self.tail == self.head: 
            self.tail = self.tail.prev
        del self.dict[node.key]
        self.head = self.head.next 
        
    def get(self, key: int) -> int:
        if key in self.dict.keys():
            node = self.dict[key]
            value = node.val
            self.deleteNode(key)
            self.addNode(key, value)
            return value
        else: 
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            node = self.dict[key]
            self.deleteNode(key)
            self.addNode(key, value)
        else: 
            self.addNode(key, value)
        if len(self.dict) > self.cap: 
            self.popNode()
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)