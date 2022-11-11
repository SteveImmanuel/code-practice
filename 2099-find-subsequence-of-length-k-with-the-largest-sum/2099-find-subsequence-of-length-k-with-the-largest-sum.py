class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        max_sub = []
        for _ in range(k):
            max_sub.append(heapq.heappop(heap))
        max_sub.sort(key=lambda x:x[1])
        return list(map(lambda x:-x[0], max_sub))
        
        # return max_sum
        