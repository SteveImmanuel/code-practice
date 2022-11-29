import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.counter = 0
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            pos = self.dict.pop(val)
            last_item = self.arr.pop()
            
            if pos != len(self.arr):
                self.arr[pos] = last_item
                self.dict[last_item] = pos
            
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
