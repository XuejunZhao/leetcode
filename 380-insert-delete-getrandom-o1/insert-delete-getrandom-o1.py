class RandomizedSet:

    def __init__(self):
        self.set = []
        self.val2idx = {}

    def insert(self, val: int) -> bool:
        if val not in self.set: 
            self.set.append(val)
            self.val2idx[val] = len(self.set) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.set: 
            return False
        else:
            idx = self.val2idx[val]
            r_val = self.set[-1]
            self.set[-1], self.set[idx] = self.set[idx], self.set[-1]
            self.val2idx[val] = len(self.set) - 1
            self.val2idx[r_val] = idx
            self.set.pop(-1)
            del self.val2idx[val]
            return True

    def getRandom(self) -> int:
        return self.set[random.randint(0,len(self.set)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()