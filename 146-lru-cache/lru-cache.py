class LRUCache:
    class LinkNode:
        def __init__(self,key=0,val=0, pre=None, next=None):
            self.key = key 
            self.val = val 
            self.pre = pre 
            self.next = next 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.cacheTail = None
        self.cacheHead = None
        # self.cache = collections.OrderedDict()
    def addNode(self, key, value):
        node = self.LinkNode(key, value)
        if self.cacheTail: 
            node.pre = self.cacheTail
            self.cacheTail.next = node  
            self.cacheTail = node 
        else: 
            self.cacheTail = node 
            self.cacheHead = node
        self.cache[key] = node
    
    def deleteNode(self, key):
        node = self.cache[key]
        if self.cacheHead.key == key: 
            self.cacheHead = self.cacheHead.next
        if self.cacheTail.key == key: 
            self.cacheTail = self.cacheTail.pre
        if node.pre: 
            node.pre.next = node.next 
        if node.next: 
            node.next.pre = node.pre
        
    def popNode(self):
        key = self.cacheHead.key
        self.cacheHead = self.cacheHead.next 
        self.cacheHead.pre = None 
        del self.cache[key]

    
    def get(self, key: int) -> int:

        if key in self.cache.keys():
            value = self.cache[key].val
            if self.cacheTail.key != key:
                self.deleteNode(key)
                self.addNode(key, value)
            return value
        else: 
            return -1  
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache.keys():
            # self.cache.move_to_end(key)
            self.deleteNode(key)
        self.addNode(key, value)

        if len(self.cache) > self.capacity:
            self.popNode()
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)