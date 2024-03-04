class LRUCache:
    class LinkNode:
        def __init__(self,key=0,val=0, prev=None, next=None):
            self.key = key 
            self.val = val 
            self.prev = prev 
            self.next = next 

    def __init__(self, capacity: int):
        self.cap = capacity
        self.tb = dict()
        # delete the head: most recently used
        self.Head = None 
        # new add to tail
        self.Tail = None 
  
    def addNode(self, key, value):
        node = self.LinkNode(key, value)
        self.tb[key]=node
        if not self.Tail: 
            self.Head = node 
            self.Tail = node 
        else:
            self.Tail.next = node
            node.prev = self.Tail
            self.Tail = node

    def deleteNode(self, key):
        node = self.tb[key]
        del self.tb[key]
        if node == self.Tail: 
            self.Tail = node.prev
        if node == self.Head:
            self.Head = node.next 
        if node.next: 
            node.next.prev = node.prev
        if node.prev: 
            node.prev.next = node.next 
        
        
    def popNode(self):
        node = self.Head
        key = node.key
        del self.tb[key]
        # print (key)
        # print (self.Tail.key)
        if node == self.Tail: 
            self.Tail = None 
            self.Head = None
        else:
            self.Head = node.next
            if node.next: 
                self.Head.prev = None
            print (self.Head.key)
    
    def get(self, key: int) -> int:
        if key in self.tb.keys(): 
            node = self.tb[key]
            self.deleteNode(key)
            value = node.val
            self.addNode(key, value)
            return value
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        # print (key)
        # print (self.tb.keys())
        if key not in self.tb.keys() and len(self.tb) < self.cap : 
            self.addNode(key, value)
        elif key not in self.tb.keys() and len(self.tb) >= self.cap : 
            self.popNode()
            self.addNode(key, value)
        else: 
            node = self.tb[key]
            self.deleteNode(key)
            self.addNode(key, value)
        # print (self.tb.keys())




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)