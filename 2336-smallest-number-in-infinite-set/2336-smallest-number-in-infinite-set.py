class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1,1001)]
        self.set = set(self.heap)
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        self.set.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)