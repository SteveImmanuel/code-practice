class Solution:
    def largestInteger(self, num: int) -> int:
        odd_heap = []
        even_heap = []
        pos = []
        
        while num > 0:
            unit = num % 10
            if unit % 2 == 0:
                heapq.heappush(even_heap, -unit)
                pos.append(True)
            else:
                heapq.heappush(odd_heap, -unit)
                pos.append(False)
            num //= 10
        
        res = 0
        
        for i in range(len(pos)-1, -1, -1):
            if pos[i]:
                item = -heapq.heappop(even_heap)
            else:
                item = -heapq.heappop(odd_heap)
            
            res = res * 10 + item
        
        return res