class RandomizedCollection:
    def __init__(self):
        self.dict = defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        exist = val not in self.dict 
        self.dict[val].add(len(self.arr))
        self.arr.append(val)
        
        return exist

    def remove(self, val: int) -> bool:
        if val in self.dict:
            pos = self.dict[val].pop()
            last_item = self.arr.pop()
            
            if pos != len(self.arr):
                self.arr[pos] = last_item
                self.dict[last_item].remove(len(self.arr))
                self.dict[last_item].add(pos)
            if len(self.dict[val]) == 0:
                del self.dict[val]
            
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()