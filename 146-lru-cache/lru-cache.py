class Doublelist:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next = None
        self.prev = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = None
        self.tail = None
    
    def add_node(self, key, val):
        added_node = Doublelist(key, val)
        if not self.head: 
            self.head = added_node 
            self.tail = added_node
        else: 
            self.tail.next = added_node
            added_node.prev = self.tail
            self.tail = added_node
        self.dict[key] = added_node

    def delete_node(self, key):
        deleted_node = self.dict[key]
        if deleted_node.next:
            deleted_node.next.prev = deleted_node.prev
        
        if deleted_node.prev:
            deleted_node.prev.next = deleted_node.next
        if deleted_node == self.tail: 
            self.tail = deleted_node.prev
        if deleted_node == self.head: 
            self.head = deleted_node.next 
            
        del self.dict[key]

    def get(self, key: int) -> int:
        if key in self.dict: 
            val = self.dict[key].val
            self.delete_node(key)
            self.add_node(key,val)
            return val
        else: 
            return -1 
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict: 
            # val = self.dict[key].val
            self.delete_node(key)
        
        self.add_node(key,value)
        if len(self.dict) > self.capacity:
            node = self.head 
            if self.tail == self.head:
                self.tail = self.tail.prev
            del self.dict[node.key]
            self.head = self.head.next


        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)