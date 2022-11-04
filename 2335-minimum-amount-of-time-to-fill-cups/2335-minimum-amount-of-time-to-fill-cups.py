class Solution:
    def fillCups(self, amount: List[int]) -> int:
        remain = [-x for x in amount]
        heapq.heapify(remain)
        
        total = 0
        while len(remain) > 0:
            cup1 = -heapq.heappop(remain)
            if cup1 > 0:
                if len(remain) > 0:
                    cup2 = -heapq.heappop(remain)
                    cup2 -= 1
                    if cup2 > 0:
                        heapq.heappush(remain, -cup2)
                cup1 -= 1
                if cup1 > 0:
                    heapq.heappush(remain, -cup1)
                total += 1
        return total
            