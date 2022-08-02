# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []
        for row in matrix:
            for el in row:
                if len(max_heap) < k:
                    heapq.heappush(max_heap, -el)
                else:
                    biggest_el = -heapq.heappop(max_heap)
                    if el < biggest_el:
                        heapq.heappush(max_heap, -el)
                    else:
                        heapq.heappush(max_heap, -biggest_el)
        return -heapq.heappop(max_heap)
sol = Solution()
matrix = [[-5]]
k = 1
print(sol.kthSmallest(matrix, k))