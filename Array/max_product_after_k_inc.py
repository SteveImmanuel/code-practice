# https://leetcode.com/contest/weekly-contest-288/problems/maximum-product-after-k-increments/
from typing import List
import heapq
import time
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k

        arr = []
        for num in nums:
            heapq.heappush(arr, num)

        for _ in range(k):
            smallest_el = heapq.heappop(arr) + 1
            heapq.heappush(arr, smallest_el)
        elapsed += time.time()

        mul = 1
        for num in arr:
            # trick for fast modulo multiply (ab mod m) = (a mod m)(b mod m) mod m
            if mul >= 1000000007:
                mul %= 1000000007
            mul *= num
        return mul % (1000000007)
sol = Solution()
nums = [24,5,64,53,26,38]
k = 54
print(sol.maximumProduct(nums, k))