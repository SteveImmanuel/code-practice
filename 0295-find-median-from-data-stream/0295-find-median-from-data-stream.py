class MedianFinder:

    def __init__(self):
        self.smaller_half = []
        self.bigger_half = []

    def addNum(self, num: int) -> None:
        if len(self.smaller_half) == 0 or num <= -self.smaller_half[0]:
            heapq.heappush(self.smaller_half, -num)
        else:
            heapq.heappush(self.bigger_half, num)
        
        if len(self.smaller_half) > len(self.bigger_half) + 1:
            heapq.heappush(self.bigger_half, -heapq.heappop(self.smaller_half))
        elif len(self.bigger_half) > len(self.smaller_half) + 1:
            heapq.heappush(self.smaller_half, -heapq.heappop(self.bigger_half))

    def findMedian(self) -> float:
        if len(self.smaller_half) > len(self.bigger_half):
            return -self.smaller_half[0]
        elif len(self.bigger_half) > len(self.smaller_half):
            return self.bigger_half[0]
        else:
            return (-self.smaller_half[0] + self.bigger_half[0]) / 2
            

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()